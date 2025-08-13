import argparse
from typing import Optional, Sequence

from constants.constants import ExportFormat, Messages


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=Messages.HELP_DESCRIPTION)
    parser.add_argument("--rooms", required=True, help=Messages.ROOMS_HELP)
    parser.add_argument("--students", required=True, help=Messages.STUDENTS_HELP)
    parser.add_argument(
        "--format",
        choices=[format.value for format in ExportFormat],
        required=True,
        help=Messages.FORMAT_HELP,
    )
    parser.add_argument("--output", required=True, help=Messages.OUTPUT_HELP)
    return parser


def parse_args(argv: Optional[Sequence[str]] = None):
    parser = build_parser()
    return parser.parse_args(args=argv)
