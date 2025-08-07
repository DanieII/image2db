from models import Records
from typing import Any
from abc import ABC, abstractmethod
from supabase import create_client


class DatabaseInserter(ABC):
    @abstractmethod
    def insert(self, data: Records):
        pass


class SupabaseInserter(DatabaseInserter):
    def __init__(self, url: str, key: str):
        self.supabase = create_client(url, key)

    def insert(self, data: Records) -> Any:
        table_name = ""
        to_insert = [item.model_dump() for item in data.records]

        try:
            response = self.supabase.table(table_name).insert(to_insert).execute()

            return response.data
        except Exception as e:
            raise e
