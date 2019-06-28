
# Covnert American Express CSVs to YNAB

For my personal finance, I use an app called <a href="https://ynab.com/referral/?ref=PreCBGSWL1digXGL&utm_source=customer_referral">You Need A Budget</a>, or YNAB.
It works pretty well for my needs, but seems to regularly have problems importing 
transactions from my American Express card.  In a fit of frustration, I built a 
little app to conver the AmEx CSV format to the format that YNAB needs, and thought 
I would share it here.


## Usage

`./convert-amex-to-ynab.py ./sample.csv`


## Bugs

- Sometimes YNAB has difficulty parsing transaction dates, but it will ask you to confirm
- Sometimes YNAB doesn't correctly de-dup transactions.  In that case, just sort by date, look for duplicate numbers, and delete one.



## Resources

- <a href="https://docs.youneedabudget.com/article/921-formatting-csv-file">YNAB documentation on importing CSV files</a>



