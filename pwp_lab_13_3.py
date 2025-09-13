# Write a Python program to read data from a CSV file data.csv and print each row to the console.

import csv
with open (r"C:\Users\PV shreyan\OneDrive\Documents\data.csv", 'r') as f1:
    reader = csv.reader (f1)
    for row in reader:
        print (row)
