// Copyright (c) 2022, Rafael Ruben and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Estudiante", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('Estudiante', {
    refresh(frm) {

        frm.add_custom_button('Mostrar Nombre', () => {
            frappe.msgprint(frm.doc.nombre, "Nombre de Estudiante")
        })
        frm.add_custom_button('Mostrar Edad', () => {
            frappe.msgprint(""+frm.doc.edad,"Edad del Estudiante")
        })

    },
    onload: function(frm) {
        frm.set_query('Estudiante', function(doc) {
            return {
                filters: {
                    "is_group": 1,
                    "edad": doc.edad
                }
            };
        });
    },
});

// filters: [{
	// 	fieldname: "company",
	// 	fieldtype:"Select",
	// 	options: erpnext.utils.get_tree_options("company"),
	// 	label: __("Company"),
	// 	default: erpnext.utils.get_tree_default("company")
	// }],

