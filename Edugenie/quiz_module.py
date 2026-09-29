import re
import json
from gemini_service import GeminiError, generate_gemini_content

class QuizGenerationError(RuntimeError):
    """A quiz could not be generated or parsed."""


def clean_json_block(text: str) -> str:
    """Remove Markdown ```json code fences and surrounding noise."""
    cleaned = re.sub(r"```(?:json)?\s*([\s\S]*?)```", r"\1", text).strip()
    return cleaned

def generate_quiz(text: str) -> list:
    """Generates 3 multiple-choice questions in JSON format based on a topic or text."""
    prompt = f"""You are a quiz generator.

From the following passage or topic, create 3 multiple-choice questions. Each question should include:
- A "question"
- A list of 4 "options"
- A correct "answer" that must exactly match one of the options.

Format your output as **valid JSON**, like this:
[
  {{
    "question": "What is ...?",
    "options": ["Option A", "Option B", "Option C", "Option D"],
    "answer": "Option A"
  }}
]

Passage:
{text}"""

    try:
        quiz_text = generate_gemini_content(prompt, response_mime_type="application/json")
            
        cleaned_text = clean_json_block(quiz_text)
        
        # In case there's additional text before or after the JSON list
        match = re.search(r'(\[[\s\S]*\])', cleaned_text)
        if match:
            cleaned_text = match.group(1)
            
        quiz_json = json.loads(cleaned_text)
        questions = quiz_json if isinstance(quiz_json, list) else [quiz_json]
        if not questions or any(
            not isinstance(question, dict)
            or not question.get("question")
            or not isinstance(question.get("options"), list)
            or question.get("answer") not in question.get("options", [])
            for question in questions
        ):
            raise QuizGenerationError("Gemini returned an invalid quiz. Please try again.")
        return questions
    except GeminiError as exc:
        raise QuizGenerationError(str(exc)) from exc
    except json.JSONDecodeError as exc:
        raise QuizGenerationError("Gemini returned an invalid quiz format. Please try again.") from exc
