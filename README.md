# mining-scripts

Setting up Google API and keys to communicate with Sheets

1. Go to https://console.developers.google.com/
2. Create a new project, and enable the Google Sheets API for your project.
3. In the API & Services > Credentials area, create credentials for your project. For a script running on your own machine, you'll use a service account.
4. Go to manage service accounts and click the 3 dots under Actions. Navigate to Manage keys and create a new key in JSON format. Save this to your local machine.
5. Share your Google Sheets spreadsheet with the email address of your service account (found in the JSON file or in service accounts).

# Installing the files on your VM

1. Once you're SSH'd into your virtual machine, run the following command:
	
	scp ~/FILE-PATH-TO-JSON root@IP-OF-VM:/root

	replacing the capitals with the local file path and IP address of your virtual machine

2. Download from github using the following command:

   gitclone https://github.com/n0comply/stake-update.git

3. cd stake-update and run mover.sh

# Configuring the Sheets API

1. cd scripts
2. nano sheets.py
3. Replace the capitals with the file name of your .json file in the following string:

creds = Credentials.from_service_account_file('/root/YOUR-JSON-KEY.json', scopes=["https://www.googleapis.com/auth/spreadsheets"])

4. Replace the spreadsheet ID in the following string:

spreadsheetId='YOUR-SPREADSHEET-ID'

5. Choose the cell which the data is outputted to in the following string (default to cell B2):

range='Sheet1!B2'


6. run install.sh and use ctrl+c to close pm2 logs when they appear. Leave the script to run and you should get Stake updates pushed every 5 mins!


