// Copyright (c) 2023, Deepak Kumar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Biochar Labs', {
	setup: function(frm) {
		frm.set_query("address", function(doc) {
			return {
				filters: {
					"link_doctype": doc.doctype,
					"link_name": doc.name
				}
			};
		});
	},
	
	refresh: function(frm) {
		frappe.dynamic_link = { doc: frm.doc, fieldname: 'name', doctype: frm.doctype }
		unhide_field(['address_html','contact_html']);
		frappe.contacts.render_address_and_contact(frm);
	},

	// address: function(frm) {
	// 	if (frm.doc.address) {
	// 		frappe.call({
	// 			method: 'frappe.contacts.doctype.address.address.get_address_display',
	// 			args: {
	// 				"address_dict": frm.doc.supplier_primary_address
	// 			},
	// 			callback: function(r) {
	// 				frm.set_value("primary_address", r.message);
	// 			}
	// 		});
	// 	}
	// 	if (!frm.doc.supplier_primary_address) {
	// 		frm.set_value("primary_address", "");
	// 	}
	// },
});
