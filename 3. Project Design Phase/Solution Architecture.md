# Solution Architecture

| Field | Details |
| --- | --- |
| Project Title | EduGenie: Your Smart Budget & Recommendation Assistant |
| Team ID | SWTID-2026-6825 |
| Team Size | 5 |
| Team Leader | Soniya C |
| Team Members | Megala, S Lavanya, Nanthini A, Nithiya Shree R J |


## Architecture Diagram

```
+------------------+      +--------------------+      +----------------------+
|  Presentation    | ---> |  Application Layer | ---> |  Data Layer          |
|  Streamlit UI    |      |  Python Services   |      |  SQLite Database     |
|  (Dashboard,     |      |  - Auth Service    |      |  (Users, Budgets,    |
|   Chat, Forms)   | <--- |  - Expense Service |      |   Expenses,          |
+------------------+      |  - Budget Alerts   |      |   Resources, Chats)  |
                          |  - Recommender     |      +----------------------+
                          |  - AI Chat Service |
                          +---------+----------+
                                    |
                                    v
                          +--------------------+
                          |  Google Gemini API |
                          +--------------------+
```

## Component Description

| Component | Responsibility | Technology | Owner |
| --- | --- | --- | --- |
| UI Layer | Forms, dashboard, chat window | Streamlit, Plotly | Nanthini A |
| Auth and Expense Service | Login, expense CRUD, validation | Python, SQLite | S Lavanya |
| Recommendation and Categorisation Engine | Budget-aware suggestions, category prediction | pandas, scikit-learn | Megala |
| AI Chat Service | Prompt building and Gemini API calls | Gemini API | Soniya C |
| Testing and Quality | Test cases and bug tracking | pytest | Nithiya Shree R J |
