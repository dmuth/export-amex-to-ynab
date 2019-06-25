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
# Flip the sign on the amount because charges are expenses, not income.
#
for row in csv:
	date = row[0]
	payee = row[2]
	amount = "{:.2f}".format(float(row[7]) * -1)
	print('{},"{}",,{}'.format(date, payee, amount))

f.close()


