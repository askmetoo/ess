# Copyright (c) 2013, fitsterp and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.utils import cint, get_datetime

def execute(filters=None):
	columns, data = [], []
	columns = get_columns(filters)
	data = get_data(filters)
	return columns, data

def get_columns(filters=None):
	return [
		{
			"label": _("Date"),
			"fieldtype": "Date",
			"fieldname": "attendance_date",
			"width": 90
		},
		{
			"label": _("Employee"),
			"fieldtype": "Link",
			"fieldname": "employee",
			"options": "Employee",
			"width": 100
		},
		{
			"label": _("Shift"),
			"fieldtype": "Data",
			"fieldname": "shift",
			"width": 100
		},
		{
			"label": _("Working Hours"),
			"fieldtype": "Float",
			"fieldname": "working_hours",
			"width": 100
		},
		{
			"label": _("Punch In"),
			"fieldtype": "Float",
			"fieldname": "in_time",
			"width": 100
		},
		{
			"label": _("Punch Out"),
			"fieldtype": "Float",
			"fieldname": "out_time",
			"width": 100
		},
		{
			"label": _("Overtime"),
			"fieldtype": "Float",
			"fieldname": "overtime",
			"width": 140
		},
		{
			"label": _("Deficit Time"),
			"fieldtype": "Float",
			"fieldname": "undertime",
			"width": 140
		},
		{
			"label": _("Late Entry"),
			"fieldtype": "Float",
			"fieldname": "late_entry",
			"width": 140
		},
		{
			"label": _("Early Exit"),
			"fieldtype": "Float",
			"fieldname": "early_exit",
			"width": 140
		}
	]

def get_conditions(filters):
	conditions = ''
	if filters.get('employee'):
		conditions += "AND so_item.employee = %s" %frappe.db.escape(filters.employee)

	return conditions

def time_diff_in_hours(start, end):
    return round((end-start).total_seconds() / 3600, 1)

def get_data(filters=None):
	conditions = get_conditions(filters)
	attendance = frappe.db.sql('''select attendance_date, shift,employee, working_hours, in_time, out_time from `tabAttendance`  {0}'''.format(conditions),as_dict=True)

    def update_shift_details(attendance_dict):
        shift_start_time = frappe.db.get_value("Shift Type",attendance_dict['shift'],'start_time')
        shift_end_time = frappe.db.get_value("Shift Type",attendance_dict['shift'],'end_time')
        shift_time_in_hours = time_diff_in_hours(shift_start_time,shift_end_time)
        attendance_dict['shift_time_in_hours'] = shift_time_in_hours
        varriance_in_working_hours = 
	# if attendance:
	# 	for i in attendance:
    #         if i['shift']:

			# i['date']=i['time'].date()
	return attendance


def get_check_in_out_log(attendance, shift):
    pass
    # in_log , out_log
    # shift_doc = frappe.get_
    # employee_checkin = frappe.db.get_all('Employee Checkin',filters={'attendance':attendance,''})
