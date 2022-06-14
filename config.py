import pygsheets

bot_token = ""

tg_bot_database = ""
tg_bot_user = ""
tg_bot_password = ""
tg_bot_host = ""
tg_bot_port = ""

eventlog_database = ""
eventlog_user = ""
eventlog_password = ""
eventlog_host = ""
eventlog_port = ""

client = pygsheets.authorize(service_account_file=)
sheet = client.open_by_key()
work_sheet = sheet.worksheet_by_title('customer_numbers')
