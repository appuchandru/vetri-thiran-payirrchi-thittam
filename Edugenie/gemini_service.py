import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv(Path(__file__).resolve().with_name(".env"))

DEFAULT_MODEL = "gemini-flash-lite-latest"
FALLBACK_MODELS = (
    "gemini-3.8-flash-lite",
    "gemini-3.5-flash-lite",
    "gemini-flash-latest",
)


class GeminiError(RuntimeError):
    """A safe-to-display Gemini configuration or request error."""


def generate_gemini_content(prompt: str, *, response_mime_type: str | None = None) -> str:
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    if not api_key or api_key.lower() in {
        "your_gemini_api_key_here",
        "your_actual_gemini_api_key",
        "replace_me",
    }:
        raise GeminiError("GEMINI_API_KEY is not configured in the .env file.")

    model = os.getenv("GEMINI_MODEL", DEFAULT_MODEL).strip() or DEFAULT_MODEL
    config = types.GenerateContentConfig(response_mime_type=response_mime_type) if response_mime_type else None
    try:
        client = genai.Client(api_key=api_key)
        try:
            response = None
            last_error = None
            retryable_statuses = {404, 408, 429, 500, 502, 503, 504}
            for candidate in dict.fromkeys((model, *FALLBACK_MODELS)):
                try:
                    response = client.models.generate_content(
                        model=candidate,
                        contents=prompt,
                        config=config,
                    )
                    break
                except Exception as exc:
                    last_error = exc
                    if getattr(exc, "code", None) not in retryable_statuses:
                        break
            if response is None:
                status = getattr(last_error, "code", None)
                if status == 404:
                    raise GeminiError(
                        "The configured Gemini model is unavailable. Remove or update GEMINI_MODEL in .env."
                    ) from last_error
                if status in {408, 429, 500, 502, 503, 504}:
                    raise GeminiError(
                        "Gemini is temporarily busy. Please try again shortly."
                    ) from last_error
                raise GeminiError(
                    "Gemini rejected the request. Check the API key, model, and API permissions."
                ) from last_error
        finally:
            client.close()
    except GeminiError:
        raise
    except Exception as exc:
        raise GeminiError(
            "Gemini request failed. Check network access, API permissions, and GEMINI_MODEL."
        ) from exc

    content = response.text
    if not content or not content.strip():
        raise GeminiError("Gemini returned an empty response. Please try again.")
    return content.strip()