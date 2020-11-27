import gspread
from oauth2client.service_account import ServiceAccountCredentials

newspreadsheet = "attendee-list"
newcsv = "csvfile"
email =  "redhat-email"
scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(credentials)

spreadsheet = client.create(newspreadsheet)
spreadsheet = client.open(newspreadsheet)
spreadsheet.share(email, perm_type='user', role= 'writer', notify=True , email_message= "A new Ansible Attendee List has been made.")

with open(newcsv, 'r') as file_obj:
    content = file_obj.read()
    client.import_csv(spreadsheet.id, data=content)
