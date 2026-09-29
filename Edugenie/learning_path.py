from gemini_service import GeminiError, generate_gemini_content

def get_learning_recommendations(topic: str) -> str:
    """Generates structured, progressive learning recommendations for a given topic."""
    prompt = f"""You are an AI tutor. The student wants to learn about: {topic}.
Suggest a structured and adaptive learning path including key topics, order of learning, and resources (videos, books, tutorials).
Include beginner, intermediate, and advanced levels if needed."""

    try:
        return generate_gemini_content(prompt)
    except GeminiError as exc:
        return f"❌ Error occurred: {exc}"
