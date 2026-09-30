# Coding & Solution

| Field | Details |
| --- | --- |
| Project Title | EduGenie: Your Smart Budget & Recommendation Assistant |
| Team ID | SWTID-2026-6825 |
| Team Size | 5 |
| Team Leader | Soniya C |
| Team Members | Megala, S Lavanya, Nanthini A, Nithiya Shree R J |


## Module Development Details

| Module | File | Description | Key Functions | Developer |
| --- | --- | --- | --- | --- |
| Main App | app.py | Entry point, page navigation | main(), render_sidebar() | Nanthini A |
| Authentication | auth.py | Register, login, password hashing | register_user(), login_user() | S Lavanya |
| Database | database.py | SQLite connection and table creation | init_db(), get_connection() | S Lavanya |
| Expense Manager | expenses.py | Add, update, delete, list expenses | add_expense(), get_expenses() | S Lavanya |
| Budget Manager | budget.py | Set budget, compute usage, raise alerts | set_budget(), check_alert() | Megala |
| Categoriser | categorizer.py | Predict category from description | predict_category() | Megala |
| Recommender | recommender.py | Filter and rank resources by budget and interest | recommend_resources() | Megala |
| AI Assistant | ai_chat.py | Build prompt and call Gemini API | build_prompt(), ask_gemini() | Soniya C |
| Dashboard | dashboard.py | Charts and summaries | spending_chart(), budget_meter() | Nanthini A |
| Savings Planner | savings.py | Savings goals and progress | create_goal(), goal_progress() | S Lavanya |

## Database Schema

| Table | Columns |
| --- | --- |
| users | id, name, email, password_hash, created_at |
| budgets | id, user_id, month, total_budget, category_limits |
| expenses | id, user_id, amount, category, description, date |
| resources | id, title, type, category, price, rating, link |
| goals | id, user_id, goal_name, target_amount, saved_amount, deadline |
| chat_history | id, user_id, question, answer, timestamp |

## Sample Code Snippet (Budget Alert)

```python
def check_alert(spent, budget):
    usage = (spent / budget) * 100 if budget else 0
    if usage >= 100:
        return "Budget exceeded! Please review your expenses."
    if usage >= 80:
        return "Warning: You have used 80% of your budget."
    return "You are within budget."
```
