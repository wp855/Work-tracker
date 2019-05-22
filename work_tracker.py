from send_email import *
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ['https://www.googleapis.com/auth/drive','https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('trackercreds.json',scope)
client = gspread.authorize(creds)
sheet = client.open('Action-Item-Tracker').sheet1

assginee = sheet.col_values(1)[1:]
task = sheet.col_values(2)[1:]
deadline = sheet.col_values(3)[1:]
current_status = sheet.col_values(4)[1:]


mem  = {}
for a in assginee:
	mem[a] = {
		"tasks":[],
	}

for task_value in sheet.get_all_values()[1:]:
	mem[task_value[0]]["tasks"].append({"task":task_value[1], "status":task_value[3]})

def get_tasks(members):
	for member in  members:

		send_email(member, mem[member], members[member])

    