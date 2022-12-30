import frappe

DOC = ["Sales Invoice", "POS Invoice"]


def after_install():
    for doctype in DOC:
        if not frappe.db.exists({"doctype": "Custom Field", "dt": doctype, "fieldtype": "Link", "fieldname": "personajur"}):
            pj = frappe.get_doc(
                {
                    "doctype": "Custom Field",
                    "dt": doctype,
                    "fieldtype": "Link",
                    "label": "Persona Jurídica",
                    "fieldname": "personajur",
                    "insert_after": "naming_series",
                    "options": "Persona Juridica",
                    "reqd": 1,
                }
            )
            pj.insert()
