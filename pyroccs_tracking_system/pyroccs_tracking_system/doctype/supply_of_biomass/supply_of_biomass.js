// Copyright (c) 2023, Deepak Kumar and contributors
// For license information, please see license.txt

frappe.ui.form.on('Supply of Biomass', {
	refresh: function(frm) {
		if (frm.doc.biomass_supply==="Select Source") {
			frm.set_df_property("supply_source","hidden", 0)
			frm.set_df_property("distance_to_plant","hidden", 0)
		} else {
			frm.set_df_property("supply_source","hidden", 1) 
			frm.set_df_property("distance_to_plant","hidden", 1)
		}
	},
	biomass_supply: function(frm) {
	// show supply source if "Select Source"
		if (frm.doc.biomass_supply==="Select Source") {
			frm.set_df_property("supply_source","hidden", 0)
			frm.set_df_property("distance_to_plant","hidden", 0)
		} else {
			frm.set_df_property("supply_source","hidden", 1) 
			frm.set_df_property("distance_to_plant","hidden", 1)
		}
	}
});
