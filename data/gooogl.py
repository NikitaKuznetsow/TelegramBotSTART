import httplib2
from pprint import pprint
import googleapiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

CREDENTIALS_FILE = 'crec.json'
spreadsheet_id = '1RuCM7l3O1SPtPupu86mkmh-8AkfoN-K1gTDe9b7BhxY'
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE,
                                                               ['https://www.googleapis.com/auth/spreadsheets',
                                                                'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = googleapiclient.discovery.build('sheets', 'v4', http=httpAuth)

values = service.spreadsheets().values().get(
    spreadsheetId = spreadsheet_id,
    range='A1:E10',
    majorDimension='COLUMNS'
).execute()
print(values['values'][2])
