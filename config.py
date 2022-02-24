import pygsheets

bot_token = "5246307613:AAEl-YRYmzyGcnqynUfZwjU-eP_agnTfNqY"

tg_bot_database = "db_tg_bot"
tg_bot_user = "tg_bot_raw_user"
tg_bot_password = "%9d[Z8c=J}Zc"
tg_bot_host = "127.0.0.1"
tg_bot_port = "5432"

eventlog_database = "db_eventlog"
eventlog_user = "postgres"
eventlog_password = "Ac3r753614"
eventlog_host = "127.0.0.1"
eventlog_port = "5432"

client = pygsheets.authorize(service_account_file='dark-pipe-338808-d5b8d22ab578.json')
sheet = client.open_by_key('1D-gMdwuzN2dTGOGBbt74RAKtMCD_ZvauGQ4_D3AAET4')
work_sheet = sheet.worksheet_by_title('customer_numbers')
