import uvicorn
from fastapi import Depends, FastAPI, Response, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import Page, add_pagination

from sqlalchemy.ext.asyncio import AsyncSession
from db.connection import Base, engine
from db.get_db import get_db
from db.models.contact import Contact

from schemas.contact import ContactIn, ContactOut

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def on_startup() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.post("/contacts", response_model=ContactOut)
async def create_contact(
    contact: ContactIn, response: Response, db: AsyncSession = Depends(get_db)
):
    response.status_code = status.HTTP_201_CREATED
    return await Contact.create(contact, db)


@app.get("/contacts/{contact_id}", response_model=ContactOut)
async def get_contact(contact_id: int, db: AsyncSession = Depends(get_db)):
    contact = await Contact.get(contact_id, db)

    if not contact:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Not found")
    return contact


@app.get("/contacts", response_model=Page[ContactOut])
async def get_contacts(
    sorting: str = "first_name",
    searching: str = "",
    db: AsyncSession = Depends(get_db),
):
    if sorting not in ["first_name", "last_name", "phone", "email", "created_at"]:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Incorrect sorting")
    return await Contact.get_all(sorting, searching, db)


@app.put("/contacts/{contact_id}", response_model=ContactOut)
async def update_contact(
    contact_id: int, contact: ContactIn, db: AsyncSession = Depends(get_db)
):
    return await Contact.update(contact_id, contact, db)


@app.delete("/contacts/{contact_id}", response_model=str)
async def delete_contacts(contact_id: int, db: AsyncSession = Depends(get_db)):
    await Contact.delete(contact_id, db)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


add_pagination(app)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
