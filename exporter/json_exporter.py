import json
from dataclasses import asdict
from typing import List

from exporter.base import Exporter
from models import Room


class JsonExporter(Exporter):
    def export(self, data: List[Room], file_path: str) -> None:
        dict_data = [asdict(room) for room in data]
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(dict_data, f, indent=4)


