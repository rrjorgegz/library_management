import frappe
from frappe.utils import now_datetime

"""
En el decorador whitelist usar las flags del framework

allow_guest = False|True

para restringir el acceso

"""
@frappe.whitelist(allow_guest=False)
def add_estudiante(nombre, edad, sexo):
	"""
	Agregar mensaje de respuesta
	"""
	if not nombre or not edad or not sexo:
		return {"success": False, "msg": "El nombre la edad y el sexo son obligatorios"}

	x1 = frappe.new_doc("Estudiante")
	x1.name = nombre
	x1.nombre = nombre
	x1.edad = str(edad)
	x1.sexo = sexo
	x1.insert()
	"""
	Agregar mensaje de respuesta
	"""
	return {"success": True, "msg": "Estudiante Agregado"}



@frappe.whitelist(allow_guest=False)
def get_estudiante():
	#return frappe.db.sql("select nombre,edad,sexo from tabEstudiante")
	"""
	Utilizar las funciones del framework para el acceso a datos, no es recomendable llenar de consultas sql
	el código del API ni la lógica del negocio. Sólo se utiliza el sql cuando no queda más remedio.
	"""
	return frappe.db.get_list('Estudiante', fields=['nombre', 'edad', 'sexo'])


@frappe.whitelist(allow_guest=False)
def set_estudiante(name, nombre, edad, sexo):
	frappe.db.set_value(
		"Estudiante", name, {"nombre": nombre, "edad": str(edad), "sexo": sexo}
	)


@frappe.whitelist(allow_guest=False)
def del_estudiante(name):
	frappe.db.delete("Estudiante", {"name": name})
	"""
	Agregar mensaje de respuesta
	"""
	return {"success": True, "msg": "Estudiante: {0} eliminado".format(name)}


@frappe.whitelist(allow_guest=False)
def hora_server():
	return {
		"hora del servidor ": f"{now_datetime().hour}:{now_datetime().minute}:{now_datetime().second}"
	}


@frappe.whitelist(allow_guest=False)
def lista_asignaturas(name):
	"""
	asg = frappe.db.sql("select * from tabAsignatura")
	lista_asignaturas = []
	for x in asg:
		if x[14] == name:
			asignatura = {}
			asignatura["nombre"] = x[7]
			lista_asignaturas.append(asignatura)
	"""

	"""
	Utilizar las funciones del framework para el acceso a datos, no es recomendable llenar de consultas sql
	el código del API ni la lógica del negocio. Sólo se utiliza el sql cuando no queda más remedio.
	"""

	asign = frappe.db.get_list('Asignatura', fields=['nombre'], filters={"parent": name})
	return {"success": True, "lista_asignaturas ": asign}


@frappe.whitelist(allow_guest=False)
def lista_estudiante(nombre):
#	est = frappe.db.sql("select * from tabEstudiante")

#	asig = frappe.db.sql("select * from tabAsignatura")	
#	list_est=[]
#	for x1 in asig:
#		if x1[7]==nombre: 
#			list_est.append(x1)  

	students_prents = frappe.db.get_list('Asignatura', fields=['parent'], filters={"nombre": nombre})
	students = []
	for est in students_prents:
		ee = frappe.get_doc('Estudiante', est['parent']).nombre
		if not ee in students:
			students.append(ee)

	return {"success": True,"lista_asignaturas": students}
