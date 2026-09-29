# EduGenie: Google Gemini Powered Learning Assistant 🎓✨

EduGenie is an AI-powered educational assistant designed to simplify learning through generative AI. Built with **FastAPI** for the backend and a modern **HTML5 + CSS3 + Vanilla JavaScript** frontend.

---

## 🚀 Features & Modules

1. **Ask a Question (Q&A)**: Get concise, accurate answers powered by Google Gemini.
2. **Concept Explanation**: Simplified, beginner-friendly explanations of complex academic concepts (supports both local `MBZUAI/LaMini-Flan-T5-783M` and Gemini cloud fallback).
3. **Paragraph Summarization**: Condense long text and articles for fast revision.
4. **Interactive Quiz Generation**: Generate 3-question multiple-choice quizzes (MCQs) with instant evaluation and feedback.
5. **Personalized Learning Recommendations**: Structured learning roadmaps from beginner to advanced with recommended tutorials, books, and videos.

---

## 📁 Project Architecture

```
EduGenie/
├── main.py                   # FastAPI application & route controllers
├── qna.py                    # Gemini question answering module (/qa)
├── explanation_module.py     # Concept explanation module (/explain)
├── summary_module.py         # Text summarization module (/summarize)
├── quiz_module.py            # Quiz generation module (/quiz)
├── learning_path.py          # Learning recommendation module (/learn/recommendations)
├── templates/
│   └── index.html            # Frontend UI with live interactive forms
├── static/
│   └── style.css             # Responsive styling
├── requirements.txt          # Project dependencies
├── .env                      # API key configuration
└── .env.example              # Environment variables template
```

---

## 🛠️ API Endpoints

| Method | Endpoint | Description | Query / Body Params |
|---|---|---|---|
| `GET` | `/` | Web Interface | None |
| `GET` | `/qa` | Question Answering | `?question=<query>` |
| `POST` | `/explain` | Concept Explanation | `{"topic": "<topic>"}` |
| `POST` | `/summarize` | Paragraph Summary | `{"text": "<passage>"}` |
| `POST` | `/quiz` | MCQ Quiz Generator | `{"text": "<topic_or_text>"}` |
| `GET` | `/learn/recommendations` | Learning Roadmap | `?topic=<topic>` |

---

## ⚙️ Setup & Execution

### 1. Configure Gemini API Key
Obtain an API key from [Google AI Studio](https://aistudio.google.com/) and add it to your `.env` file:
```env
GEMINI_API_KEY=your_actual_gemini_api_key
```

### 2. Run the Application
Start the Uvicorn ASGI server:
```bash
uvicorn main:app --reload
```
or run with Python:
```bash
python main.py
```

### 3. Open in Browser
Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)
