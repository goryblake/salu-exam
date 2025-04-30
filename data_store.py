from uuid import UUID
from project.models import Clinic
from project.exam_type_enum import ExamTypeEnum
from datetime import time

class DataStore:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init()
        return cls._instance

    def _init(self):
        self.clinics: dict[UUID, Clinic] = {}

    def add_clinic(self, clinic: Clinic):
        self.clinics[clinic.clinic_id] = clinic

    def get_clinic(self, clinic_id: UUID) -> Clinic:
        return self.clinics.get(clinic_id)

    def initialize_sample_data(self):
        from uuid import uuid4
        # Clínica A
        clinic_a = Clinic(
            clinic_id=uuid4(),
            name="Clínica Central",
            open_time=time(8, 0),
            close_time=time(18, 0),
            supported_exams=[
                ExamTypeEnum.GENERAL_CHECKUP,
                ExamTypeEnum.BLOOD_TEST,
                ExamTypeEnum.XRAY
            ]
        )
        self.add_clinic(clinic_a)

        # Clínica B
        clinic_b = Clinic(
            clinic_id=uuid4(),
            name="Clínica Oeste",
            open_time=time(7, 30),
            close_time=time(17, 30),
            supported_exams=[
                ExamTypeEnum.GENERAL_CHECKUP,
                ExamTypeEnum.ECG,
                ExamTypeEnum.BLOOD_TEST
            ]
        )
        self.add_clinic(clinic_b)
