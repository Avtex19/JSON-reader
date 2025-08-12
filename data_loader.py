from abc import ABC, abstractmethod
from typing import List, Type, TypeVar
from dataclasses import is_dataclass
import json

T = TypeVar('T')


class DataLoader(ABC):
    @abstractmethod
    def load(self, file_path: str) -> List[T]:
        pass


class JsonDataLoader(DataLoader):
    def __init__(self, data_type: Type[T]):
        if not is_dataclass(data_type):
            raise TypeError("data_type must be a dataclass")
        self.data_type = data_type

    def load(self, file_path: str) -> List[T]:
        with open(file_path, "r", encoding="utf-8") as file:
            raw_list = json.load(file)
        return [self.data_type(**item) for item in raw_list]
