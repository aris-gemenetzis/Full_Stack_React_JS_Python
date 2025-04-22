from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
client = OpenAI()

app = FastAPI()


origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/", tags=["root"])
async def read_root() -> dict:
    return {"message": "Welcome to your tax form."}


class Form(BaseModel):
    company: str
    revenue: float
    costs: float
    id: int


forms_dict = {
    0: Form(company='deloitte', revenue=10, costs=5, id=0)
}


def call_openai(form: Form) -> str:
    response = client.responses.create(
    model="gpt-4.1",
    input=f'Compute the Corcporate Income Tax (CIT) for a Greek company with revenue {form.revenue} million euros and costs {form.costs} million euros.'
)
    print(response.output_text)
    return(response.output_text)


@app.get('/')
async def main():
    return {'msg': 'Welcome to your tax form.'}


@app.get('/forms')
async def get_forms() -> dict:
    return {"data": forms_dict}


@app.get('/forms/{form_id}')
async def query_form_by_id(form_id: int) -> Form:
    if form_id not in forms_dict:
        raise HTTPException(status_code=404, detail='Item not found')
    return forms_dict[form_id]


@app.post("/forms/add")
async def add_form(form: Form) -> dict[str, Form | str]:
    if int(form.id) in forms_dict:
        raise HTTPException(status_code=400, detail=f"Company with {form.id=} already exists.")
    forms_dict[form.id] = form
    text = call_openai(form) # test call
    # return {"added": form}
    return {"added": form, "text": text}


@app.put("/forms/{form_id}")
async def update_form(form: Form) -> dict[str, Form | str]:
    if form.id not in forms_dict:
            raise HTTPException(status_code=404, detail=f"Item with {form.id=} does not exist.")
    forms_dict[form.id] = form
    text = call_openai(form) # test call
    # return {"updated": form}
    return {"updated": form, "text": text}


@app.delete("/forms/{form_id}")
async def delete_form(form_id: int) -> dict[str, Form]:
    if form_id not in forms_dict:
        raise HTTPException(
            status_code=404, detail=f"Form with {form_id=} does not exist."
        )

    form = forms_dict.pop(form_id)
    return {"deleted": form}
