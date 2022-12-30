# Copyright (c) 2022, Rafael Ruben and Contributors
# See license.txt

# import frappe
from frappe.tests.utils import FrappeTestCase

def create_estudiante():
	test_estudiante = frappe.get_doc(
		{
			"name": "prueba1",
			"nombre": "Juan",
			"edad": "14",
			"sexo": "A", 
		}
	)
	test_estudiante.insert()
	return test_estudiante

class TestEstudiante(FrappeTestCase):
   
	def setUpClass():
		frappe.db.delete("Estudiante", {"nombre": 'Juan'})

	def setUp(self):
		self.test_estudiante = create_estudiante()  
		estud = frappe.get_doc({"doctype": "Estudiante"})

		try:
			estud.validate()
		except AttributeError:
			msg = "Estudiante.validate() failed value M or F"
			self.fail(msg=msg)
 