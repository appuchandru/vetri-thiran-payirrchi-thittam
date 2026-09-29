from gemini_service import GeminiError, generate_gemini_content

def answer_question_with_gemini(question: str) -> str:
    """Answers general and academic questions using Google Gemini."""
    try:
        return generate_gemini_content(question)
    except GeminiError as exc:
        return f"⚠️ Error in QnA: {exc}"
