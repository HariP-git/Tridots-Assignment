#hooks.py


doc_events = {
    "student": {
        "validate": "cafe_management.api.validate_student"
    }
}

#api.py

def validate_student(doc, method):
    frappe.msgprint("Student validation executed!")


