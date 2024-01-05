# Copyright (c) 2024, Mustafa M. Younus and contributors
# For license information, please see license.txt

# import frappe
from frappe import _
import frappe

def execute(filters=None):
    columns = [_("Room"), _("Reservation Count")]

    data = []

    # Fetch data from the database
    room_data = frappe.db.sql("""
        SELECT r.room_number, COUNT(r.room_number) as reservation_count
        FROM `tabGuest` r
        GROUP BY r.room_number
    """, as_dict=True)

    for room in room_data:
        data.append([room.room, room.reservation_count])

    return columns, data

