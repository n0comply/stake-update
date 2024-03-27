import re
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# Log file path
log_file_path = "/root/logs/output.log"

# Function to extract stake amounts from the log file
def extract_stake_amounts(log_file_path):
    stake_amounts = []
    stake_pattern = re.compile(r"Stake: (\d+\.\d+)")
    with open(log_file_path, 'r') as file:
        for line in file:
            match = stake_pattern.search(line)
            if match:
                # Append the first found stake amount and break
                stake_amounts.append(match.group(1))
                break  # Assumes you only want the first occurrence per script execution
    return stake_amounts

# Function to update Google Sheet
def update_google_sheet(values):
    creds = Credentials.from_service_account_file('/root/YOUR-JSON-KEY.json', scopes=["https://www.googleapis.com/auth/spreadsheets"])
    service = build('sheets', 'v4', credentials=creds)
    body = {
        'values': values
    }
    # Use 'update' method instead of 'append' and specify the exact cell 'B2'
    result = service.spreadsheets().values().update(
        spreadsheetId='YOUR-SPREADSHEET-ID',
        range='Sheet1!B2',  # Updated to target only B2
        valueInputOption='USER_ENTERED', body=body).execute()
    print(f"{result.get('updatedCells')} cells updated.")

# Main function
def main(log_file_path):
    stake_amounts = extract_stake_amounts(log_file_path)
    # Assuming you want to update the sheet with the first found stake amount
    if stake_amounts:
        values = [[stake_amounts[0]]]  # Update to only include the first found amount
        update_google_sheet(values)

if __name__ == "__main__":
    main(log_file_path)
