import os
from gemini_service import GeminiError, generate_gemini_content

# Global variables for lazy loading local model
explain_tokenizer = None
explain_model = None
local_model_loaded = False

def init_local_model():
    """Attempts to load local MBZUAI/LaMini-Flan-T5-783M model if transformers & torch are installed."""
    global explain_tokenizer, explain_model, local_model_loaded
    if local_model_loaded:
        return True
    if os.getenv("EDUGENIE_USE_LOCAL_EXPLANATION_MODEL", "").strip().lower() not in {"1", "true", "yes", "on"}:
        return False
    try:
        from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
        import torch
        print("⏳ Loading local explanation model (MBZUAI/LaMini-Flan-T5-783M)...")
        explain_tokenizer = AutoTokenizer.from_pretrained("MBZUAI/LaMini-Flan-T5-783M")
        explain_model = AutoModelForSeq2SeqLM.from_pretrained("MBZUAI/LaMini-Flan-T5-783M")
        local_model_loaded = True
        print("✅ Local explanation model loaded successfully.")
        return True
    except Exception as e:
        print(f"ℹ️ Local LaMini model not loaded ({e}). Using Gemini fallback.")
        return False

def explain_topic(topic: str) -> str:
    """Explains a topic in simple terms for a school student."""
    input_text = f"Explain the concept of '{topic}' in a simple and clear way for a school student."
    
    # Check if local model can be used
    if init_local_model() and explain_tokenizer is not None and explain_model is not None:
        try:
            import torch
            inputs = explain_tokenizer(input_text, return_tensors="pt")
            outputs = explain_model.generate(
                **inputs,
                max_new_tokens=150,
                temperature=0.7,
                top_k=50,
                top_p=0.95,
                do_sample=True
            )
            explanation = explain_tokenizer.decode(outputs[0], skip_special_tokens=True)
            return explanation
        except Exception as e:
            print(f"Error during local model generation: {e}")
            # Fall through to Gemini
            
    try:
        return generate_gemini_content(input_text)
    except GeminiError as exc:
        return f"⚠️ Error in Explanation: {exc}"
