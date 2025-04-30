from datetime import datetime
from uuid import UUID
from project.data_store import DataStore
from project.models import Exam
from project.exam_type_enum import ExamTypeEnum

class ExamSchedulerClass:
    def __init__(self):
        self.store = DataStore()
        if not self.store.clinics:
            self.store.initialize_sample_data()

    def execute(
        self,
        employee_id: UUID,
        clinic_id: UUID,
        exam_type: ExamTypeEnum,
        exam_start: datetime
    ) -> tuple[bool, str]:
        clinic = self.store.get_clinic(clinic_id)
        if not clinic:
            return False, "Clínica não encontrada"


        if exam_type not in clinic.supported_exams:
            return False, "Tipo de exame não oferecido pela clínica"


        start_time = exam_start.time()
        end_time = (exam_start + Exam.DURATION).time()
        if start_time < clinic.open_time or end_time > clinic.close_time:
            return False, "Exame não pode ser agendado fora do horário de funcionamento"


        new_exam = Exam(employee_id, clinic_id, exam_type, exam_start)
        for existing in clinic.scheduled_exams:
            if new_exam.overlaps(existing):
                return False, "Exame não pode ser agendado devido a um conflito de horário"


        clinic.scheduled_exams.append(new_exam)
        return True, "Exame agendado com sucesso"
