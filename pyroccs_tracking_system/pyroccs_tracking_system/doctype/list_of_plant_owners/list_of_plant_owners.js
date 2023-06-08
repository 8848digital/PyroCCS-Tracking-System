// Copyright (c) 2023, Deepak Kumar and contributors
// For license information, please see license.txt

frappe.ui.form.on('List of Plant Owners', {
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
		frappe.dynamic_link = { doc: frm.doc, fieldname: 'name', doctype: 'List of Plant Owners' }
	}
});
