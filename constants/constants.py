from enum import Enum


class ExportFormat(Enum):
    """Supported export formats"""
    JSON = "json"
    XML = "xml"


class FileExtensions:
    """File extension constants"""
    JSON = ".json"
    XML = ".xml"


class Directories:
    """Directory constants"""
    OUTPUT = "output"


class Messages:
    """Application messages"""
    SUCCESS_EXPORT = "Data combined and exported successfully to {output_path}"
    HELP_DESCRIPTION = "Combine rooms and students, export as JSON or XML."
    ROOMS_HELP = "Rooms JSON file path"
    STUDENTS_HELP = "Students JSON file path"
    FORMAT_HELP = "Output format"
    OUTPUT_HELP = "Output file path"


class XmlConstants:
    """XML-specific constants"""
    ROOT_ELEMENT = "rooms"
