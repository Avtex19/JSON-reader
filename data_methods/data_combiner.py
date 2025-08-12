from typing import List
from models import Student, Room


class DataCombiner:
    def __init__(self, rooms: List[Room], students: List[Student]):
        self.rooms = rooms
        self.students = students

    def combine(self) -> List[Room]:
        room_dict = {room.id: room for room in self.rooms}

        for student in self.students:
            if student.room in room_dict:
                room_dict[student.room].students.append(student)

        return list(room_dict.values())
