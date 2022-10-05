import datetime

from fastapi_pagination.ext.async_sqlalchemy import paginate

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from db.connection import Base

from schemas.contact import ContactIn


class Contact(Base):
    __tablename__ = "contact"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100))
    phone = Column(String(12), nullable=False)
    email = Column(String(320))
    created_at = Column(DateTime, default=datetime.datetime.now())

    def __repr__(self):
        return f"{self.first_name} {self.last_name} - +{self.phone}"

    @classmethod
    async def create(cls, contact: ContactIn, db: AsyncSession):
        new_contact = cls(**vars(contact))
        db.add(new_contact)
        await db.commit()

        return new_contact

    @classmethod
    async def get(cls, contact_id: int, db: AsyncSession):
        result = await db.execute(select(cls).where(cls.id == contact_id).limit(1))
        fetch = result.fetchone()

        if not fetch:
            return None

        return fetch[0]

    @classmethod
    async def get_all(cls, sorting: str, searching: str, db: AsyncSession):
        return await paginate(
            db,
            (
                select(cls)
                .where(
                    cls.first_name.ilike(f"%{searching}%")
                    | cls.last_name.ilike(f"%{searching}%")
                    | cls.phone.ilike(f"%{searching}%")
                    | cls.email.ilike(f"%{searching}%")
                )
                .order_by(sorting)
            ),
        )

    @classmethod
    async def update(cls, contact_id: int, contact: ContactIn, db: AsyncSession):
        await db.execute(
            update(cls).where(cls.id == contact_id).values(**vars(contact))
        )
        await db.commit()

        return await cls.get(contact_id, db)

    @classmethod
    async def delete(cls, contact_id: int, db: AsyncSession):
        await db.execute(delete(cls).where(cls.id == contact_id))
        await db.commit()
