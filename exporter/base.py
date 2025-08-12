from abc import ABC, abstractmethod
from typing import List
from models import Room


class Exporter(ABC):
    @abstractmethod
    def export(self, data: List[Room], file_path: str) -> None:
        pass
