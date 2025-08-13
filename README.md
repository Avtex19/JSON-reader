# JSON Reader - Room and Student Data Processor

A Python application that combines room and student data from JSON files and exports the results in JSON or XML format. Built following SOLID principles with a clean, extensible architecture.

## Features

- **Data Loading**: Loads student and room data from JSON files
- **Data Combination**: Combines rooms with their assigned students
- **Multiple Export Formats**: Supports JSON and XML output formats
- **Command Line Interface**: Easy-to-use CLI with proper argument parsing
- **SOLID Principles**: Clean, maintainable, and extensible code architecture
- **Type Safety**: Full type hints for better code reliability

## Requirements

- Python 3.7+
- `dicttoxml` library (for XML export)

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd JSON-reader
   ```

2. **Install dependencies:**
   ```bash
   pip3 install dicttoxml
   ```

## Project Structure

```
JSON-reader/
├── main.py                 # Main application entry point
├── constants/              # Application constants and enums
│   ├── __init__.py
│   └── constants.py
├── cli/                    # Command-line interface configuration
│   ├── __init__.py
│   └── cli.py
├── models/                 # Data models
│   ├── __init__.py
│   └── models.py          # Student and Room data models
├── loader/                # Data loading functionality
│   ├── __init__.py
│   └── data_loader.py     # Data loading implementations
├── data_methods/          # Data processing functionality
│   ├── __init__.py
│   ├── data_combiner.py   # Data combination logic
│   └── data_processor.py  # Data processing utilities
├── exporter/              # Export functionality
│   ├── __init__.py
│   ├── base.py           # Abstract exporter base class
│   ├── json_exporter.py  # JSON export implementation
│   └── xml_exporter.py   # XML export implementation
├── examples_json/         # Sample input data
│   ├── students.json     # Sample student data
│   └── rooms.json        # Sample room data
├── output/               # Generated output files
│   ├── combined.json     # Sample JSON output
│   └── combined.xml      # Sample XML output
└── README.md            # This file
```

## Usage

### Command Line Interface

The application accepts the following command-line arguments:

```bash
python3 main.py --rooms ROOMS_FILE --students STUDENTS_FILE --format {json,xml} --output OUTPUT_FILE
```

#### Arguments:
- `--rooms`: Path to the rooms JSON file (required)
- `--students`: Path to the students JSON file (required)
- `--format`: Output format - either "json" or "xml" (required)
- `--output`: Path for the output file (required)

### Examples

**Export as JSON:**
```bash
python3 main.py --rooms examples_json/rooms.json --students examples_json/students.json --format json --output combined.json
```

**Export as XML:**
```bash
python3 main.py --rooms examples_json/rooms.json --students examples_json/students.json --format xml --output combined.xml
```

**View help:**
```bash
python3 main.py --help
```

## Data Format

### Input Files

**students.json:**
```json
[
    {
        "id": 0,
        "name": "John Doe",
        "room": 101
    }
]
```

**rooms.json:**
```json
[
    {
        "id": 101,
        "name": "Room #101"
    }
]
```

### Output Format

**JSON Output:**
```json
[
    {
        "id": 101,
        "name": "Room #101",
        "students": [
            {
                "id": 0,
                "name": "John Doe",
                "room": 101
            }
        ]
    }
]
```

**XML Output:**
```xml
<?xml version="1.0" encoding="UTF-8" ?>
<rooms>
    <item>
        <id>101</id>
        <name>Room #101</name>
        <students>
            <item>
                <id>0</id>
                <name>John Doe</name>
                <room>101</room>
            </item>
        </students>
    </item>
</rooms>
```

## Architecture

The application follows SOLID principles and clean architecture:

### Core Components

1. **Data Models** (`models.py`)
   - `Student`: Represents student data
   - `Room`: Represents room data with associated students

2. **Data Loading** (`loader/data_loader.py`)
   - `DataLoader`: Abstract base class for data loading
   - `JsonDataLoader`: Concrete implementation for JSON files

3. **Data Processing** (`data_methods/data_combiner.py`)
   - `DataCombiner`: Combines room and student data

4. **CLI Configuration** (`cli/cli.py`)
   - Centralized argument parsing and CLI setup

5. **Constants and Enums** (`constants/constants.py`)
   - Shared enums, directory names, messages, and other constants

6. **Data Export** (`exporter/`)
   - `Exporter`: Abstract base class for data export
   - `JsonExporter`: JSON export implementation
   - `XmlExporter`: XML export implementation

### SOLID Principles Implementation

- **Single Responsibility**: Each class has one clear purpose
- **Open/Closed**: Easy to extend with new export formats or data sources
- **Liskov Substitution**: Concrete implementations can substitute abstract classes
- **Interface Segregation**: Clean, focused interfaces
- **Dependency Inversion**: High-level modules depend on abstractions

## Testing

The application has been tested with:
- Valid JSON input files
- Both JSON and XML export formats
- Command-line argument parsing
- Error handling for missing files
- Data combination logic

## Sample Data

The repository includes sample data files:
- `examples_json/students.json`: Contains 10,000+ student records
- `examples_json/rooms.json`: Contains 1,000 room records
- `output/combined.json`: Sample JSON output
- `output/combined.xml`: Sample XML output
