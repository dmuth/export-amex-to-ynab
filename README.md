
# Covnert American Express CSVs to YNAB

For my personal finance, I use an app called <a href="https://ynab.com/referral/?ref=PreCBGSWL1digXGL&utm_source=customer_referral">You Need A Budget</a>, or YNAB.
It works pretty well for my needs, but seems to regularly have problems importing 
transactions from my American Express card.  In a fit of frustration, I built a 
little app to conver the AmEx CSV format to the format that YNAB needs, and thought 
I would share it here.


## Downloading CSV data from Amex

- Log into Amex
- Click on "Statements and Activity"
- Click on "Recent Activity" dropdown and choose dates for which you'd like to download transactions.
- Click the download button second from the right
- Click "Current View"
- Choose CSV and do NOT check the checkbox
- Transactions will now be downloaded


## Usage

`./convert-amex-to-ynab.py ./sample.csv`

Or, to run the script without cloning this repo:

`curl -s https://raw.githubusercontent.com/dmuth/export-amex-to-ynab/master/convert-amex-to-ynab.py | python3 - ./sample.csv > ynab.csv`

Either invocation will read a CSV file that you downloaded form AmEx and write to stdout
a CSV file that YNAB can understand.


## Uploading converted CSV data to YNAB

- Run the script as detailed above and put the output into a file called `ynab.csv` or similar.
- Log into YNAB in your web browser and go into "All Accounts"
- Click "Import" and click "Choose File"
- Choose the account to import to and click the "Import" button.
- The transactions will be uploaded and you should now see them in YNAB.




## Bugs

- Sometimes YNAB has difficulty parsing transaction dates, but it will ask you to confirm
- Sometimes YNAB doesn't correctly de-dup transactions.  In that case, just sort by date, look for duplicate numbers, and delete one.



## Resources

- <a href="https://docs.youneedabudget.com/article/921-formatting-csv-file">YNAB documentation on importing CSV files</a>



