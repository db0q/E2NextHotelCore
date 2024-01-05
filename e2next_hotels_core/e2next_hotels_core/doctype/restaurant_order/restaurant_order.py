# Copyright (c) 2024, Mustafa M. Younus and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe

class RestaurantOrder(Document):
    def on_submit(self):
        self.your_datetime_field = frappe.utils.now()
        # Set the date-time field to the current date and
    pass