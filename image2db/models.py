from pydantic import BaseModel


class Record(BaseModel):
    pass


class Records(BaseModel):
    records: list[Record]
