# Performance Testing

| Field | Details |
| --- | --- |
| Project Title | EduGenie: Your Smart Budget & Recommendation Assistant |
| Team ID | SWTID-2026-6825 |
| Team Size | 5 |
| Team Leader | Soniya C |
| Team Members | Megala, S Lavanya, Nanthini A, Nithiya Shree R J |


## Functional Test Cases

| TC ID | Module | Test Scenario | Test Steps | Expected Result | Status |
| --- | --- | --- | --- | --- | --- |
| TC-01 | Authentication | Register with valid details | Enter name, email, password and submit | Account created and user redirected to login | Ready to execute |
| TC-02 | Authentication | Login with wrong password | Enter valid email and wrong password | Error message shown, access denied | Ready to execute |
| TC-03 | Budget | Set monthly budget | Enter budget amount and save | Budget saved and shown on dashboard | Ready to execute |
| TC-04 | Expenses | Add a valid expense | Enter amount, description, date and save | Expense listed and totals updated | Ready to execute |
| TC-05 | Expenses | Add expense with negative amount | Enter -100 and save | Validation error shown | Ready to execute |
| TC-06 | Categoriser | Auto category suggestion | Enter description "Python course" | Category suggested as Education | Ready to execute |
| TC-07 | Alerts | 80% budget alert | Add expenses reaching 80% of budget | Warning alert displayed | Ready to execute |
| TC-08 | Alerts | Budget exceeded alert | Add expenses above budget | Budget exceeded message displayed | Ready to execute |
| TC-09 | Recommender | Budget-based suggestions | Set budget 500 and request courses | Only resources priced within 500 shown | Ready to execute |
| TC-10 | AI Chat | Ask a saving tip | Ask "How can I save more this month?" | Relevant advice generated | Ready to execute |
| TC-11 | AI Chat | API failure handling | Use invalid API key | Friendly error message, app does not crash | Ready to execute |
| TC-12 | Savings Goal | Track goal progress | Create goal and add savings | Progress percentage updated | Ready to execute |

## Performance Test Cases

| PT ID | Parameter | Test Condition | Target |
| --- | --- | --- | --- |
| PT-01 | Page Load Time | Open dashboard with 100 expense records | Under 3 seconds |
| PT-02 | Chat Response Time | Send a normal chat query | Under 8 seconds |
| PT-03 | Recommendation Speed | Filter 500 resources by budget | Under 2 seconds |
| PT-04 | Database Query Time | Fetch monthly expenses | Under 1 second |
| PT-05 | Concurrent Users | 10 users using the app together | No crash and no data mix-up |
| PT-06 | Data Volume | 1,000 expense entries for one user | Charts render without lag |

## Test Ownership

| Activity | Owner |
| --- | --- |
| Test case design and execution | Nithiya Shree R J |
| Bug fixing (backend) | S Lavanya, Megala |
| Bug fixing (UI) | Nanthini A |
| Bug fixing (AI integration) and final sign-off | Soniya C |
