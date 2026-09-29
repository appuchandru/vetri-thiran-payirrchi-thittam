from gemini_service import GeminiError, generate_gemini_content

def summarize_text(text: str) -> str:
    """Summarizes text into concise, easy-to-understand content."""
    prompt = f"Summarize the following text in simple language:\n\n{text}"
    
    try:
        return generate_gemini_content(prompt)
    except GeminiError as exc:
        return f"⚠️ Error in Summary: {exc}"
