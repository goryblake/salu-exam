from datetime import datetime
from uuid import uuid4

from project.exam_scheduler import ExamSchedulerClass
from project.exam_type_enum import ExamTypeEnum

if __name__ == "__main__":
    scheduler = ExamSchedulerClass()


    print("Clínicas disponíveis:")
    for cid, clinic in scheduler.store.clinics.items():
        print(f"  {cid} — {clinic.name} ({clinic.open_time.strftime('%H:%M')}–{clinic.close_time.strftime('%H:%M')})")


    employee_id = uuid4()

    clinic_id = list(scheduler.store.clinics.keys())[0]
    exam_type = ExamTypeEnum.GENERAL_CHECKUP
    exam_start = datetime(2023, 10, 15, 14, 0)

    result, message = scheduler.execute(employee_id, clinic_id, exam_type, exam_start)
    print("\nResultado do agendamento:")
    print(f"  {message}")
