# EduGenie Demo Video Script

**Estimated runtime:** about 3 minutes 40 seconds  
**Format:** screen recording with narration

## Before Recording

- Start the FastAPI app with `python main.py`, or run `python -m uvicorn main:app --host 127.0.0.1 --port 8001` if port 8000 is occupied.
- Open the matching local URL in a browser and confirm the dashboard loads.
- Keep `.env` closed and out of the recording. Never show or read the Gemini API key.
- Keep the prepared sample inputs below nearby. Wait for each response before moving to the next feature.
- `requirements.txt`, `.env.example`, `.gitignore`, and `README.md` are supporting project files; they are not part of the timed source-code walkthrough.

## Opening | 0:00–0:08

**On screen:** Show the EduGenie project, then switch to the application browser tab.

**Say:** “This is EduGenie, a learning assistant built with FastAPI and Gemini. I’ll briefly show how its source files fit together, then demonstrate each feature in the dashboard.”

## Source Files | 0:08–1:50

Each source-file segment is approximately 10–15 seconds.

### `main.py` | 0:08–0:20

**On screen:** Open `main.py`; point to the app setup and route definitions.

**Say:** “`main.py` creates the FastAPI app, serves the dashboard and static files, and connects the API routes to Q&A, explanation, summary, quiz, and learning recommendations.”

### `gemini_service.py` | 0:20–0:32

**On screen:** Show the default model and shared generation function; do not open `.env`.

**Say:** “`gemini_service.py` loads the API key privately from the environment, sends prompts through Google’s Gemini SDK, and retries supported models when a model is unavailable or busy.”

### `qna.py` | 0:32–0:43

**On screen:** Show `answer_question_with_gemini`.

**Say:** “`qna.py` keeps question answering separate from the web routes. It sends the student’s question to the shared Gemini service and returns the answer or a safe error message.”

### `explanation_module.py` | 0:43–0:55

**On screen:** Show `explain_topic` and the local-model opt-in setting.

**Say:** “`explanation_module.py` turns a topic into a student-friendly explanation. Gemini is the default; an optional Transformers and Torch model can be enabled explicitly when it is installed.”

### `summary_module.py` | 0:55–1:06

**On screen:** Show `summarize_text`.

**Say:** “`summary_module.py` builds a concise-language prompt from the supplied passage and uses the shared Gemini client, keeping summarization logic out of the route and dashboard.”

### `quiz_module.py` | 1:06–1:18

**On screen:** Show the JSON prompt and answer validation.

**Say:** “`quiz_module.py` requests multiple-choice questions as JSON, parses the response, and checks that each correct answer matches an option. Invalid or unavailable responses become clear errors.”

### `learning_path.py` | 1:18–1:29

**On screen:** Show the recommendation prompt.

**Say:** “`learning_path.py` asks Gemini for an ordered learning roadmap, with beginner, intermediate, and advanced topics and suggested learning resources.”

### `templates/index.html` | 1:29–1:40

**On screen:** Show the five forms and the JavaScript event handlers.

**Say:** “`index.html` defines the five dashboard forms and browser-side interactions. JavaScript sends requests to FastAPI, displays loading and error states, renders answers, and checks quiz choices.”

### `static/style.css` | 1:40–1:50

**On screen:** Show the responsive layout and quiz styles.

**Say:** “`style.css` gives the dashboard its typography, layout, responsive controls, result panels, and quiz feedback states, so the same features remain readable across screen sizes.”

## Web Dashboard | 1:50–3:30

**Duration:** 1 minute 40 seconds, within the requested 1–2 minute walkthrough.

### Dashboard Overview | 1:50–2:02

**On screen:** Show the full page and scroll slowly through the five modules.

**Say:** “The dashboard brings all five learning tools into one page. Each module has a focused input and button, and its result appears beneath the form after processing.”

### Ask a Question | 2:02–2:20

**On screen:** In the Q&A field, enter: `How does the water cycle work?` Click **Get Answer** and show the response.

**Say:** “First, I’ll ask EduGenie a general science question. The question is sent to the Q&A endpoint, and the Gemini answer appears here with readable formatting.”

### Explanation | 2:20–2:37

**On screen:** Enter `Photosynthesis` in the explanation field and click **Explain**.

**Say:** “Next, I’ll request a simple explanation of photosynthesis. The explanation module uses Gemini by default, so it avoids downloading the optional large local model unless that mode is enabled.”

### Summary | 2:37–2:53

**On screen:** Paste the short passage below into the summary field and click **Summarize**.

> Plants use sunlight, water, and carbon dioxide to make sugar through photosynthesis. The process also releases oxygen into the air.

**Say:** “For summarization, I paste a short passage and submit it. EduGenie returns a more concise version that is easier to review.”

### Quiz | 2:53–3:15

**On screen:** Enter `The water cycle includes evaporation, condensation, and precipitation.` Click **Generate Quiz**; select an answer and click **Check Answer**.

**Say:** “The quiz tool creates multiple-choice questions from a topic or passage. I can select an option, check it immediately, and see whether it is correct. If Gemini is temporarily busy, the dashboard shows a retry message instead of fake questions.”

### Learning Recommendations | 3:15–3:30

**On screen:** Enter `learning Python` and click **Get Recommendations**.

**Say:** “Finally, I’ll request a path for learning Python. EduGenie returns an ordered set of topics and resource suggestions, helping a student decide what to study next.”

## Closing | 3:30–3:38

**On screen:** Return to the dashboard overview.

**Say:** “That’s EduGenie: a single dashboard for answers, explanations, summaries, quizzes, and personalized learning recommendations.”
# EduGenie Demo Video Script

**Estimated runtime:** about 3 minutes 40 seconds  
**Format:** screen recording with narration

## Before Recording

- Start the FastAPI app with `python main.py`, or run `python -m uvicorn main:app --host 127.0.0.1 --port 8001` if port 8000 is occupied.
- Open the matching local URL in a browser and confirm the dashboard loads.
- Keep `.env` closed and out of the recording. Never show or read the Gemini API key.
- Keep the prepared sample inputs below nearby. Wait for each response before moving to the next feature.
- `requirements.txt`, `.env.example`, `.gitignore`, and `README.md` are supporting project files; they are not part of the timed source-code walkthrough.

## Opening | 0:00–0:08

**On screen:** Show the EduGenie project, then switch to the application browser tab.

**Say:** “This is EduGenie, a learning assistant built with FastAPI and Gemini. I’ll briefly show how its source files fit together, then demonstrate each feature in the dashboard.”

## Source Files | 0:08–1:50

Each source-file segment is approximately 10–15 seconds.

### `main.py` | 0:08–0:20

**On screen:** Open `main.py`; point to the app setup and route definitions.

**Say:** “`main.py` creates the FastAPI app, serves the dashboard and static files, and connects the API routes to Q&A, explanation, summary, quiz, and learning recommendations.”

### `gemini_service.py` | 0:20–0:32

**On screen:** Show the default model and shared generation function; do not open `.env`.

**Say:** “`gemini_service.py` loads the API key privately from the environment, sends prompts through Google’s Gemini SDK, and retries supported models when a model is unavailable or busy.”

### `qna.py` | 0:32–0:43

**On screen:** Show `answer_question_with_gemini`.

**Say:** “`qna.py` keeps question answering separate from the web routes. It sends the student’s question to the shared Gemini service and returns the answer or a safe error message.”

### `explanation_module.py` | 0:43–0:55

**On screen:** Show `explain_topic` and the local-model opt-in setting.

**Say:** “`explanation_module.py` turns a topic into a student-friendly explanation. Gemini is the default; an optional Transformers and Torch model can be enabled explicitly when it is installed.”

### `summary_module.py` | 0:55–1:06

**On screen:** Show `summarize_text`.

**Say:** “`summary_module.py` builds a concise-language prompt from the supplied passage and uses the shared Gemini client, keeping summarization logic out of the route and dashboard.”

### `quiz_module.py` | 1:06–1:18

**On screen:** Show the JSON prompt and answer validation.

**Say:** “`quiz_module.py` requests multiple-choice questions as JSON, parses the response, and checks that each correct answer matches an option. Invalid or unavailable responses become clear errors.”

### `learning_path.py` | 1:18–1:29

**On screen:** Show the recommendation prompt.

**Say:** “`learning_path.py` asks Gemini for an ordered learning roadmap, with beginner, intermediate, and advanced topics and suggested learning resources.”

### `templates/index.html` | 1:29–1:40

**On screen:** Show the five forms and the JavaScript event handlers.

**Say:** “`index.html` defines the five dashboard forms and browser-side interactions. JavaScript sends requests to FastAPI, displays loading and error states, renders answers, and checks quiz choices.”

### `static/style.css` | 1:40–1:50

**On screen:** Show the responsive layout and quiz styles.

**Say:** “`style.css` gives the dashboard its typography, layout, responsive controls, result panels, and quiz feedback states, so the same features remain readable across screen sizes.”

## Web Dashboard | 1:50–3:30

**Duration:** 1 minute 40 seconds, within the requested 1–2 minute walkthrough.

### Dashboard Overview | 1:50–2:02

**On screen:** Show the full page and scroll slowly through the five modules.

**Say:** “The dashboard brings all five learning tools into one page. Each module has a focused input and button, and its result appears beneath the form after processing.”

### Ask a Question | 2:02–2:20

**On screen:** In the Q&A field, enter: `How does the water cycle work?` Click **Get Answer** and show the response.

**Say:** “First, I’ll ask EduGenie a general science question. The question is sent to the Q&A endpoint, and the Gemini answer appears here with readable formatting.”

### Explanation | 2:20–2:37

**On screen:** Enter `Photosynthesis` in the explanation field and click **Explain**.

**Say:** “Next, I’ll request a simple explanation of photosynthesis. The explanation module uses Gemini by default, so it avoids downloading the optional large local model unless that mode is enabled.”

### Summary | 2:37–2:53

**On screen:** Paste the short passage below into the summary field and click **Summarize**.

> Plants use sunlight, water, and carbon dioxide to make sugar through photosynthesis. The process also releases oxygen into the air.

**Say:** “For summarization, I paste a short passage and submit it. EduGenie returns a more concise version that is easier to review.”

### Quiz | 2:53–3:15

**On screen:** Enter `The water cycle includes evaporation, condensation, and precipitation.` Click **Generate Quiz**; select an answer and click **Check Answer**.

**Say:** “The quiz tool creates multiple-choice questions from a topic or passage. I can select an option, check it immediately, and see whether it is correct. If Gemini is temporarily busy, the dashboard shows a retry message instead of fake questions.”

### Learning Recommendations | 3:15–3:30

**On screen:** Enter `learning Python` and click **Get Recommendations**.

**Say:** “Finally, I’ll request a path for learning Python. EduGenie returns an ordered set of topics and resource suggestions, helping a student decide what to study next.”

## Closing | 3:30–3:38

**On screen:** Return to the dashboard overview.

**Say:** “That’s EduGenie: a single dashboard for answers, explanations, summaries, quizzes, and personalized learning recommendations.”
