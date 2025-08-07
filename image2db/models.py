from pydantic import BaseModel


class Record(BaseModel):
    """
    Define your data structure by inheriting from this class.

    Example:
        class Record(BaseModel):
            invoice_number: str
            amount: float
            date: str
    """

    pass


class Records(BaseModel):
    records: list[Record]
