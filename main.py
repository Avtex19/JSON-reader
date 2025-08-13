import os

from data_methods.data_combiner import DataCombiner
from loader.data_loader import JsonDataLoader
from exporter.json_exporter import JsonExporter
from exporter.xml_exporter import XmlExporter
from models import Room, Student
from constants.constants import ExportFormat, Directories, Messages
from cli.cli import parse_args


def main():
    args = parse_args()

    rooms_loader = JsonDataLoader(Room)
    students_loader = JsonDataLoader(Student)

    rooms = rooms_loader.load(args.rooms)
    students = students_loader.load(args.students)

    combiner = DataCombiner(rooms, students)
    combined = combiner.combine()

    exporters = {
        ExportFormat.JSON.value: JsonExporter(),
        ExportFormat.XML.value: XmlExporter(),
    }
    exporter = exporters[args.format]

    output_dir = os.path.join(os.getcwd(), Directories.OUTPUT)
    os.makedirs(output_dir, exist_ok=True)
    output_file_name = os.path.basename(args.output)
    output_path = os.path.join(output_dir, output_file_name)

    exporter.export(combined, output_path)

    print(Messages.SUCCESS_EXPORT.format(output_path=output_path))


if __name__ == "__main__":
    main()
