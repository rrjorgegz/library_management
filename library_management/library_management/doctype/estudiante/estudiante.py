# Copyright (c) 2022, Rafael Ruben and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Estudiante(Document):
	def validate(self):
		if self.get("sexo") != "M" and self.get("sexo") != "F":
			frappe.throw("sexo solo puede ser M or F")


@frappe.whitelist()
def alet_insert_estiduante(doc, event):
	# frappe.show_alert({message: "Estudiante {0} {1} {2} insertado.".format(doc.nombre,doc.edad,doc.sexo),indicator: 'yellow' });
	frappe.msgprint(
		f"Estudiante {doc.nombre} {doc.edad} {doc.sexo} insertado.",
		title="Warning!",
		indicator="orange",
		alert=1,
	)
