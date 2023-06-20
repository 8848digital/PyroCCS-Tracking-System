# Copyright (c) 2023, Deepak Kumar and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.contacts.address_and_contact import (
	delete_contact_and_address,
	load_address_and_contact,
)


class BiocharLabs(Document):
	

	def onload(self):
		"""Load address and contacts in `__onload`"""
		load_address_and_contact(self)

	def on_trash(self):
		if self.contact:
			self.db_set("contact", None)
		if self.address:
			self.db_set("address", None)

		delete_contact_and_address(self.doctype, self.name)
