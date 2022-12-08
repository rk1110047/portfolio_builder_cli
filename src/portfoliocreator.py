import asyncio
from datetime import datetime
import gspread
import xlsxwriter
import subprocess
import oauth2client.service_account

myScope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
myCreds = oauth2client.service_account.ServiceAccountCredentials.from_json_keyfile_name('./googleCred.json', myScope)

client = gspread.authorize(myCreds)
spreadsheet = client.open_by_key('1JHLliHqIdwHoK-gaRta-XQIlPlFeaDVaihHdwFWTdJI')

import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, FileFormatType

"""
Export Excel To SpreadSheet
Refrence : https://blog.aspose.com/cells/export-excel-data-to-google-sheets-in-python/

Install Java
Refrence : https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/How-do-I-install-Java-on-Ubuntu
"""

def export_xlsx_to_spreadsheet():
    # Load Excel workbook
    wb = Workbook()

    # Get worksheets collection
    collection = wb.getWorksheets()
    collectionCount = collection.getCount()

    # Get workbook and first sheet's name
    spreadsheetName = wb.getFileName()
    firstSheetName = collection.get(0).getName()



# async def create_portfolio_xlsx(risk_profile, heading_keys, portfolio_stock_list):
#     risk_profile = "High Risk"
#     today_date = datetime.now().date().strftime("%d %b, %Y")
#
#     worksheet = spreadsheet.get_worksheet(3)
#
#     worksheet.update_cell(1, 2, today_date)
#     worksheet.update_cell(2, 2, risk_profile)
#     heading_row = 4
#     heading_column = 1
#     for heading in heading_keys:
#         worksheet.update_cell(heading_row, heading_column, heading)
#         heading_column += 1
#
#     row = 5
#     outer_col = 1
#     serial_num = 1
#
#     for portfolio_item in portfolio_stock_list:
#         worksheet.update_cell(row, outer_col, serial_num)
#         col = outer_col + 1
#         for index in range(len(heading_keys) - 1):
#             worksheet.update_cell(row, col, portfolio_item[heading_keys[index + 1]])
#             col += 1
#         row += 1
#         serial_num += 1

# asyncio.sleep(0.05)

async def create_portfolio_xlsx(risk_profile , heading_keys, portfolio_stock_list):
    risk_profile = "High Risk"
    today_date = datetime.now().date().strftime("%d %b, %Y")
    subprocess.call(["rm", "portfolio.xlsx"])
    workbook = xlsxwriter.Workbook('portfolio.xlsx')

    worksheet = workbook.add_worksheet()

    worksheet.write(0, 1, today_date)
    worksheet.write(1, 1, risk_profile)
    heading_row = 3
    heading_column = 0
    for heading in heading_keys:
        worksheet.write(heading_row, heading_column, heading)
        heading_column += 1


    row = 4
    outer_col = 0
    serial_num = 0

    for portfolio_item in portfolio_stock_list:
        worksheet.write(row, outer_col, serial_num)
        col = outer_col + 1
        for index in range(len(heading_keys)-1):
            worksheet.write(row, col, portfolio_item[heading_keys[index + 1]])
            col += 1
        row += 1
        serial_num += 1
        # asyncio.sleep(0.05)
    workbook.close()

export_xlsx_to_spreadsheet()



# from Google import Create_Service
# import win32com.client as win32
#
# xlApp = win32.Dispatch('Excel.Application')
# wb = xlApp.Workbooks.Open(r"<Excel File Path>")
# ws = wb.Worksheets('<Worksheet Name>')
# rngData = ws.Range('A1').CurrentRegion()
#
# # Google Sheet Id
# gsheet_id = '<Google Sheet Id>'
# CLIENT_SECRET_FILE = 'client_secret.json'
# API_SERVICE_NAME = 'sheets'
# API_VERSION = 'v4'
# SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
# service = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)
#
# response = service.spreadsheets().values().append(
#     spreadsheetId=gsheet_id,
#     valueInputOption='RAW',
#     range='WorksheetName!A1',
#     body=dict(
#         majorDimension='ROWS',
#         values=rngData
#     )
# ).execute()