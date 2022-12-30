import frappe
from frappe.utils import now_datetime


@frappe.whitelist()
def add_estudiante(nombre, edad, sexo):
	x1 = frappe.new_doc("Estudiante")
	x1.name = nombre
	x1.nombre = nombre
	x1.edad = str(edad)
	x1.sexo = sexo
	x1.insert()


@frappe.whitelist()
def get_estudiante():
	return frappe.db.sql("select nombre,edad,sexo from tabEstudiante")


@frappe.whitelist()
def set_estudiante(name, nombre, edad, sexo):
	frappe.db.set_value(
		"Estudiante", name, {"nombre": nombre, "edad": str(edad), "sexo": sexo}
	)


@frappe.whitelist()
def del_estudiante(name):
	frappe.db.delete("Estudiante", {"name": name})


@frappe.whitelist()
def hora_server():
	return {
		"hora del servidor ": f"{now_datetime().hour}:{now_datetime().minute}:{now_datetime().second}"
	}


@frappe.whitelist()
def lista_asignaturas(name):
	asg = frappe.db.sql("select * from tabAsignatura")
	lista_asignaturas = []
	for x in asg:
		if x[14] == name:
			asignatura = {}
			asignatura["nombre"] = x[7]
			lista_asignaturas.append(asignatura)
	return {"lista_asignaturas ": lista_asignaturas}


@frappe.whitelist()
def lista_estudiante(nombre):
	est = frappe.db.sql("select * from tabEstudiante")

#	asig = frappe.db.sql("select * from tabAsignatura")	
#	list_est=[]
#	for x1 in asig:
#		if x1[7]==nombre: 
#			list_est.append(x1)  

	return {"lista_asignaturas ": est}
