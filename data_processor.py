from data_combiner import DataCombiner
from data_loader import DataLoader
from exporter.base import Exporter


class DataProcessor:
    def __init__(
        self,
        rooms_loader: DataLoader,
        students_loader: DataLoader,
        combiner: DataCombiner,
        exporter: Exporter,
    ):
        self.rooms_loader = rooms_loader
        self.students_loader = students_loader
        self.combiner = combiner
        self.exporter = exporter

    def process(self, rooms_file: str, students_file: str, output_file: str) -> None:
        rooms = self.rooms_loader.load(rooms_file)
        students = self.students_loader.load(students_file)
        combined = self.combiner.combine(rooms, students)
        self.exporter.export(combined, output_file)
