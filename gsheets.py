import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
def main():
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

    client = gspread.authorize(creds)

    sheet = client.open("test_project").sheet1  # Open the spreadhseet

    data = sheet.get_all_records()  # Get a list of all records
    #pprint(data)
    row = sheet.row_values(3)  # Get a specific row
    col = sheet.col_values(3)  # Get a specific column
    cell = sheet.cell(1,2).value  # Get the value of a specific cell

    insertRow = [4, "brad", "blanc"]
    sheet.insert_row(insertRow, 5)  # Insert the list as a row at index 4
    sheet.delete_row(6)
    sheet.update_cell(2,2, "Tawheed")  # Update one cell

    numRows = sheet.row_count  # Get the number of rows in the sheet

if __name__ == '__main__':
    main()          