from typing import List
from collections import defaultdict
from models import Student, Room


class DataCombiner:
    def __init__(self, rooms: List[Room], students: List[Student]):
        self.rooms = rooms
        self.students = students

    def combine(self) -> List[Room]:
        room_dict = {room.id: room for room in self.rooms}
        room_students = defaultdict(list)

        for student in self.students:
            room_students[student.room].append(student)

        for room in room_dict.values():
            room.students = room_students[room.id]

        return list(room_dict.values())
