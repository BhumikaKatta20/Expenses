from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from pydantic import BaseModel, EmailStr
from typing import Union
from datetime import date
from . import models
from . import collections as colc
# from models import *
from fastapi import Query
# from bson.objectid import ObjectId
import os

current_directory = os.getcwd()
print(current_directory)

app=FastAPI()
templates = Jinja2Templates(directory="pyfiles/templates")


from fastapi import Form

    
# uvicorn pyfiles.main:app --reload
@app.get("/AddExpense")
def read_root(request: Request):
    options=""
    op=['Baby', 'Food', 'Health', 'House', 'Ration', 'Travel', 'Unexpected']
    for i in op:
        val='<option value="'+i+'">'+i+'</option>\n'
        options+=val
      
    return templates.TemplateResponse("index.html", {"request": request, "name": "Expense Project","options":options})

@app.post("/addItem")
async def add_itemm(
    request: Request,
    date: str = Form(...),
    category: str = Form(...),
    spentOn: str = Form(...),
    amount: float = Form(...)):
    # Here, you would typically handle saving the data to a database
    # For demonstration, we'll just print it
    val={"Date": date, "Category": category, "SpentOn": spentOn, "Amount": amount}
    print(val)
    colc.addOneRecord(val)
    # Redirecting back to the expense page after processing
    return RedirectResponse(url="/AddExpense", status_code=303)
# @app.get("/addItem")
# def addItem(request: Request):
#     print(Request)
#     return "Expense Home Page"

