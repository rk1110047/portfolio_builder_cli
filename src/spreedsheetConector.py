import gspread
import asyncio
import oauth2client.service_account
from src.portfoliocreator import create_portfolio_xlsx

myScope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
myCreds = oauth2client.service_account.ServiceAccountCredentials.from_json_keyfile_name('./googleCred.json', myScope)

client = gspread.authorize(myCreds)
spreadsheet = client.open_by_key('1JHLliHqIdwHoK-gaRta-XQIlPlFeaDVaihHdwFWTdJI')
worksheet1 = spreadsheet.get_worksheet(0)
worksheet2 = spreadsheet.get_worksheet(1)
worksheet3 = spreadsheet.get_worksheet(2)

stock_list = worksheet1.get_all_records()
sector_list = worksheet2.get_all_records()
user_details = worksheet3.get_all_records()


"""
BEAUTIFYING USER PROFILE
"""
stock_keys = list(stock_list[0].keys())
print(F"Stock Keys: {stock_keys}")
Yes = 'Yes'
No = 'No'
first_item = user_details[0]
risk_profile = first_item['Risk Profile']
risk_profile_both = 'Both'
investment_amount = first_item['Investment Amount']
no_of_stocks = [int(x) for x in first_item['No. of Stocks'].split('-')]
religion = first_item['Religion Restriction']
is_shariah = False
is_jain = False
religion_check = False
religion_list = ['Shariah', 'Jain']
if religion in religion_list:
    print("Yes In Here")
    religion_check = True
    if religion == 'Shariah':
        is_shariah = True

    if religion == 'Jain':
        is_jain = True

excluded_stocks = []
excluded_sectors = []
for item in user_details:
    if item['Excluded Stocks'] != '':
        excluded_stocks.append(item['Excluded Stocks'])

    if item['Excluded Sectors'] != '':
        excluded_sectors.append(item['Excluded Sectors'])


portfolio_stocks = []


async def create_final_portfolio_list():
    stocks_added = 0
    for stock_item in stock_list:
        if (stock_item['Risk Profile'] == risk_profile or stock_item['Risk Profile'] == risk_profile_both) \
                and stock_item['Symbol'] not in excluded_stocks and stock_item['Sector'] not in excluded_sectors:

            add_to_portfolio = False

            if religion_check:
                if (is_shariah and stock_item['Allowed Shariah'] == Yes) \
                        or (is_jain and stock_item['Allowed Jain'] == Yes):
                    add_to_portfolio = True
            else:
                add_to_portfolio = True

            if add_to_portfolio:
                portfolio_stocks.append(stock_item)
                stocks_added += 1

        if stocks_added == no_of_stocks[0]:
            break


asyncio.run(create_final_portfolio_list())
asyncio.run(create_portfolio_xlsx(risk_profile, stock_keys, portfolio_stocks))
