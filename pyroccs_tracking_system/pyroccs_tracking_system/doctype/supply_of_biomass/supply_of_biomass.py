# Copyright (c) 2023, Deepak Kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class SupplyofBiomass(Document):
	

	def on_update(self):
		avg_moisture = (self.moisture_measurement_1 + self.moisture_measurement_2 + self.moisture_measurement_3 \
		  + self.moisture_measurement_4 + self.moisture_measurement_5 + self.moisture_measurement_6)/6
		frappe.db.set_value(self.doctype, self.name, 'average_moisture', avg_moisture)
		frappe.db.commit()