from abc import ABC, abstractmethod
from typing import List, Dict, Any
import json


class DataLoader(ABC):
    @abstractmethod
    def load(self, file_path: str) -> List[Dict[str, Any]]:
        pass


class JsonDataLoader(DataLoader):
    def load(self, file_path: str) -> List[Dict[str, Any]]:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
