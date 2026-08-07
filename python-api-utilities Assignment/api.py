import frappe
from frappe.utils import now

@frappe.whitelist()
def get_recent_students():

    students = frappe.get_list(
        "student",
        fields=["name", "subject_name", "teacher"],
        order_by="creation desc",
        page_length=5
    )

    for student in students:
        student["teacher_name"] = frappe.db.get_value(
            "teacher",
            student["teacher"],
            "teacher_name"
        )

    return {
        "timestamp": now(),
        "records": students
    }