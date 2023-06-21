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
		if (frm.doc.transportation_type == "Vehicle with Trailer") {
			frm.set_df_property('name_of_trailer', 'reqd', 1)
			frm.set_df_property('name_of_vehicle', 'reqd', 1)
		} else {
			frm.set_df_property('name_of_trailer', 'hidden', 1)
			frm.set_df_property('name_of_vehicle', 'hidden', 1)
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
	},
	transportation_type: function(frm) {
		if (frm.doc.transportation_type == "Vehicle with Trailer") {
			frm.set_df_property('name_of_trailer', 'reqd', 1)
			frm.set_df_property('name_of_vehicle', 'reqd', 1)
			frm.set_df_property('name_of_trailer', 'hidden', 0)
			frm.set_df_property('name_of_vehicle', 'hidden', 0)
		} else {
			frm.set_df_property('name_of_trailer', 'reqd', 0)
			frm.set_df_property('name_of_vehicle', 'reqd', 0)
			frm.set_df_property('name_of_trailer', 'hidden', 1)
			frm.set_df_property('name_of_vehicle', 'hidden', 1)
		}
	}
});
