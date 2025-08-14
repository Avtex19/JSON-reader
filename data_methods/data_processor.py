from data_methods.data_combiner import DataCombiner
from exporter.base import Exporter
from loader.data_loader import DataLoader


class DataProcessor:
    def __init__(
        self,
        rooms_loader: DataLoader,
        students_loader: DataLoader,
        exporter: Exporter,
    ):
        self.rooms_loader = rooms_loader
        self.students_loader = students_loader
        self.exporter = exporter

    def process(self, rooms_file: str, students_file: str, output_file: str) -> None:
        rooms = self.rooms_loader.load(rooms_file)
        students = self.students_loader.load(students_file)
        combiner = DataCombiner(rooms, students)
        combined = combiner.combine()
        self.exporter.export(combined, output_file)
