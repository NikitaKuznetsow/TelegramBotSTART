import googleapiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
import httplib2
CREDENTIALS_FILE = 'credentails.json'
spreadsheet_id = '1RuCM7l3O1SPtPupu86mkmh-8AkfoN-K1gTDe9b7BhxY'
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE,
                                                                   ['https://www.googleapis.com/auth/spreadsheets',
                                                                    'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = googleapiclient.discovery.build('sheets', 'v4', http=httpAuth)

def chech_table():


    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A1:G10',
        majorDimension='COLUMNS'
    ).execute()
    return(values)

def change_table(day,cell_number,task):
    results = service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheet_id, body={
        "valueInputOption": "USER_ENTERED",
        "data": [
            {"range": "{0}{1}:{0}{1}".format(day,cell_number),
             "majorDimension": "COLUMNS",             # сначала заполнять ряды, затем столбцы (т.е. самые внутренние списки в values - это ряды)
             "values": [[task]] }


        ]
    }).execute()