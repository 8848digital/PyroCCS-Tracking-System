from . import __version__ as app_version

app_name = "pyroccs_tracking_system"
app_title = "PyroCCS Tracking System"
app_publisher = "Deepak Kumar"
app_description = "PyroCCS Tracking System"
app_email = "deepakkumar@8848digital.com"
app_license = "MIT"

# Includes in <head>
# ------------------
# global
# map= "public/js/doc_map.js"
fixtures = ["Custom Field"]
# include js, css files in header of desk.html
# app_include_css = "/assets/pyroccs_tracking_system/css/pyroccs_tracking_system.css"
# app_include_js = "/assets/pyroccs_tracking_system/js/map.js"

# include js, css files in header of web template
# web_include_css = "/assets/pyroccs_tracking_system/css/pyroccs_tracking_system.css"
# web_include_js = "/assets/pyroccs_tracking_system/js/pyroccs_tracking_system.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "pyroccs_tracking_system/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"List of Biomass Supply Locations" : map}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "pyroccs_tracking_system.utils.jinja_methods",
#	"filters": "pyroccs_tracking_system.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "pyroccs_tracking_system.install.before_install"
# after_install = "pyroccs_tracking_system.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "pyroccs_tracking_system.uninstall.before_uninstall"
# after_uninstall = "pyroccs_tracking_system.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "pyroccs_tracking_system.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"pyroccs_tracking_system.tasks.all"
#	],
#	"daily": [
#		"pyroccs_tracking_system.tasks.daily"
#	],
#	"hourly": [
#		"pyroccs_tracking_system.tasks.hourly"
#	],
#	"weekly": [
#		"pyroccs_tracking_system.tasks.weekly"
#	],
#	"monthly": [
#		"pyroccs_tracking_system.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "pyroccs_tracking_system.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "pyroccs_tracking_system.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "pyroccs_tracking_system.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["pyroccs_tracking_system.utils.before_request"]
# after_request = ["pyroccs_tracking_system.utils.after_request"]

# Job Events
# ----------
# before_job = ["pyroccs_tracking_system.utils.before_job"]
# after_job = ["pyroccs_tracking_system.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"pyroccs_tracking_system.auth.validate"
# ]
