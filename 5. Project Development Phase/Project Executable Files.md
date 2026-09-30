# Project Executable Files

| Field | Details |
| --- | --- |
| Project Title | EduGenie: Your Smart Budget & Recommendation Assistant |
| Team ID | SWTID-2026-6825 |
| Team Size | 5 |
| Team Leader | Soniya C |
| Team Members | Megala, S Lavanya, Nanthini A, Nithiya Shree R J |


## Executable Files

| S.No. | File Name | Type | Purpose |
| --- | --- | --- | --- |
| 1 | app.py | Python | Launches the EduGenie application |
| 2 | requirements.txt | Text | Lists all Python dependencies |
| 3 | .env.example | Config | Template for GEMINI_API_KEY |
| 4 | database/init_db.py | Python | Creates database tables and loads sample resources |
| 5 | data/resources.csv | CSV | Sample dataset for recommendations |
| 6 | tests/test_edugenie.py | Python | Automated tests |

## How to Run

| Step | Command / Action |
| --- | --- |
| 1 | Clone the repository: git clone <repository-url> |
| 2 | Create a virtual environment: python -m venv venv |
| 3 | Activate it: venv\Scripts\activate (Windows) or source venv/bin/activate (Linux/Mac) |
| 4 | Install dependencies: pip install -r requirements.txt |
| 5 | Copy .env.example to .env and add your GEMINI_API_KEY |
| 6 | Initialise the database: python database/init_db.py |
| 7 | Start the app: streamlit run app.py |
| 8 | Open http://localhost:8501 in the browser |
