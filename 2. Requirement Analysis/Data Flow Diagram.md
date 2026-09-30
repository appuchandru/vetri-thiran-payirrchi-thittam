# Data Flow Diagram

| Field | Details |
| --- | --- |
| Project Title | EduGenie: Your Smart Budget & Recommendation Assistant |
| Team ID | SWTID-2026-6825 |
| Team Size | 5 |
| Team Leader | Soniya C |
| Team Members | Megala, S Lavanya, Nanthini A, Nithiya Shree R J |


## Level 0 (Context Diagram)

```
[Student] --> (EduGenie System) --> [Student]
                     |
                     +--> [Gemini AI API]
```

## Level 1 Data Flow

```
Student --> Login/Register --> Users DB
Student --> Expense Entry --> Validation --> Expenses DB --> Budget Checker --> Alerts --> Student
Expenses DB --> Analytics Module --> Dashboard --> Student
Student --> Chat Query --> Prompt Builder (budget + expenses context) --> Gemini AI API --> Response --> Student
Student --> Preferences --> Recommendation Engine <-- Resources DB --> Filtered Suggestions --> Student
```

## Data Flow Table

| Flow ID | Source | Process | Data Store | Destination | Data Passed |
| --- | --- | --- | --- | --- | --- |
| DF-1 | Student | Authentication | Users DB | Student | Email, password hash, session token |
| DF-2 | Student | Expense Entry and Validation | Expenses DB | Budget Checker | Amount, category, date, note |
| DF-3 | Budget Checker | Alert Generation | Budgets DB | Student | Budget used percentage, alert message |
| DF-4 | Expenses DB | Analytics | Expenses DB | Dashboard | Category totals, monthly trend |
| DF-5 | Student | Chat Prompt Builder | Expenses and Budgets DB | Gemini AI API | User question with budget context |
| DF-6 | Gemini AI API | Response Formatter | Chat History DB | Student | Generated advice text |
| DF-7 | Student | Recommendation Engine | Resources DB | Student | Interests, budget limit, ranked suggestions |
