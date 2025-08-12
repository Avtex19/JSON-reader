import argparse

from data_combiner import DataCombiner
from data_loader import JsonDataLoader
from exporter.json_exporter import JsonExporter
from exporter.xml_exporter import XmlExporter
from models import Room, Student


def parse_args():
    parser = argparse.ArgumentParser(description="Combine rooms and students, export as JSON or XML.")
    parser.add_argument("--rooms", required=True, help="Rooms JSON file path")
    parser.add_argument("--students", required=True, help="Students JSON file path")
    parser.add_argument("--format", choices=["json", "xml"], required=True, help="Output format")
    parser.add_argument("--output", required=True, help="Output file path")
    return parser.parse_args()


def main():
    args = parse_args()

    rooms_loader = JsonDataLoader(Room)
    students_loader = JsonDataLoader(Student)

    rooms = rooms_loader.load(args.rooms)
    students = students_loader.load(args.students)

    combiner = DataCombiner(rooms, students)
    combined = combiner.combine()

    exporters = {
        "json": JsonExporter(),
        "xml": XmlExporter(),
    }
    exporter = exporters[args.format]
    exporter.export(combined, args.output)

    print(f"Data combined and exported successfully to {args.output}")


if __name__ == "__main__":
    main()
