from pydantic import BaseModel
from datetime import date

class Expense(BaseModel):
    date: date
    category: str
    spent_on: str
    amount: float