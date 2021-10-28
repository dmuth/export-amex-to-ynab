#!/usr/bin/env python3

import argparse
import csv

parser = argparse.ArgumentParser(description = "An app to turn AmEx CSVs into YNAB format.")
parser.add_argument("file", type=str)
args = parser.parse_args()


f = open(args.file)

csv = csv.reader(f)

#
# Print the header that YNAB wants.
#
print("Date, Payee, Memo, Amount")

#
# Loop through rows and print in the format YNAB wants.
#
beenhere = False
for row in csv:
	
	#print(f"ROW: {row}") # Debugging

	if not beenhere:
		beenhere = True
		continue

	#
	# The date is in the format "06/01/2019  Sat", and we just
	# want the first part of that.
	#
	date = row[0]
	fields = date.split(" ")
	date = fields[0]

	payee = row[1]
	amount = row[2]

	#
	# Flip the sign on the amount because charges are expenses, not income.
	#
	amount = "{:.2f}".format(float(amount) * -1)

	#print(f"ROW: {row}") # Debugging
	print('{},"{}",,{}'.format(date, payee, amount))

f.close()


