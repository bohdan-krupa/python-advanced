from text_report import TextReport
from db.models.analyzed_text import AnalyzedText
from db.connection import Base, Session, engine

Base.metadata.create_all(engine)


class Repository:
    def __init__(self) -> None:
        self.session = Session()

    def add_analyzed_text(self, name: str, text_report: TextReport) -> None:
        new_analyzed_text = AnalyzedText(name=name, data=text_report)

        self.session.add(new_analyzed_text)
        self.session.commit()

    def get_analyzed_text(self, name: str) -> TextReport:
        text_report = next(
            iter(
                self.session.query(AnalyzedText.data)
                .order_by(AnalyzedText.id.desc())
                .where(AnalyzedText.name == name)
                .first()
                or []
            ),
            None,
        )

        return text_report
