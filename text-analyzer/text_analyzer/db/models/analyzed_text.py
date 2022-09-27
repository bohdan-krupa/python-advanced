import datetime
from sqlalchemy import Column, Integer, String, Date, PickleType
from db.connection import Base


class AnalyzedText(Base):
    __tablename__ = "analyzed_text"

    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    data = Column(PickleType, nullable=False)
    checked_date = Column(Date, default=datetime.datetime.today())

    def __repr__(self):
        return f"{self.name}"
