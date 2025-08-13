from typing import List
from dataclasses import asdict
from dicttoxml import dicttoxml

from exporter.base import Exporter
from models import Room
from constants.constants import XmlConstants


class XmlExporter(Exporter):
    def export(self, data: List[Room], file_path: str) -> None:
        data_dicts = [asdict(room) for room in data]

        xml_bytes = dicttoxml(data_dicts, custom_root=XmlConstants.ROOT_ELEMENT, attr_type=False)

        with open(file_path, "wb") as file:
            file.write(xml_bytes)
