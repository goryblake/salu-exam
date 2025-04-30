from datetime import time, datetime, timedelta
from uuid import UUID
from typing import List

from project.exam_type_enum import ExamTypeEnum

class Clinic:
    def __init__(self, clinic_id: UUID, name: str, open_time: time, close_time: time, supported_exams: List[ExamTypeEnum]):
        self.clinic_id = clinic_id
        self.name = name
        self.open_time = open_time
        self.close_time = close_time
        self.supported_exams = supported_exams
        self.scheduled_exams: List[Exam] = []

class Exam:
    DURATION = timedelta(hours=1)

    def __init__(self, employee_id: UUID, clinic_id: UUID, exam_type: ExamTypeEnum, start: datetime):
        self.employee_id = employee_id
        self.clinic_id = clinic_id
        self.exam_type = exam_type
        self.start = start
        self.end = start + Exam.DURATION

    def overlaps(self, other: "Exam") -> bool:
        return (
            self.clinic_id == other.clinic_id
            and not (self.end <= other.start or self.start >= other.end)
        )
