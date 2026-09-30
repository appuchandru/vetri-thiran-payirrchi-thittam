# Code-Layout, Readability and Reusability

| Field | Details |
| --- | --- |
| Project Title | EduGenie: Your Smart Budget & Recommendation Assistant |
| Team ID | SWTID-2026-6825 |
| Team Size | 5 |
| Team Leader | Soniya C |
| Team Members | Megala, S Lavanya, Nanthini A, Nithiya Shree R J |


## Project Folder Layout

| Path | Purpose |
| --- | --- |
| app.py | Application entry point |
| modules/ | Reusable modules (auth, expenses, budget, recommender, ai_chat, dashboard, savings) |
| data/resources.csv | Sample courses, books and tools dataset |
| database/edugenie.db | SQLite database file |
| tests/ | pytest test files |
| requirements.txt | Python dependencies |
| .env.example | Sample environment variables (no real keys) |
| README.md | Setup and usage guide |

## Coding Standards

| Area | Standard Followed |
| --- | --- |
| Naming | snake_case for functions and variables, PascalCase for classes |
| Style | PEP 8 formatting |
| Documentation | Docstring for every function and comments for complex logic |
| Modularity | One responsibility per module, no duplicated logic |
| Reusability | Shared helpers for database access, validation and API calls |
| Error Handling | try/except around database and API calls with user-friendly messages |
| Security | API keys in .env, passwords hashed with bcrypt, inputs validated |
| Version Control | Feature branches, pull requests reviewed before merge |
