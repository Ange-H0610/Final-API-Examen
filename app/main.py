from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Characteristic(BaseModel):
    ram_memory: int
    rom_memory: int


class Phone(BaseModel):
    identifier: str
    brand: str
    model: str
    characteristics: Characteristic


phones_db: List[Phone] = []

# a.
@app.get("/health")
def health_check():
    return "Ok"

# b.
@app.post("/phones", status_code=201)
def create_phones(phones: List[Phone]):
    for phone in phones:
        phones_db.append(phone)
    return {"message": "Phones added successfully"}

# c.
@app.get("/phones")
def get_phones():
    return phones_db

# d.
@app.get("/phones/{id}")
def get_phone(id: str):
    for phone in phones_db:
        if phone.identifier == id:
            return phone
    