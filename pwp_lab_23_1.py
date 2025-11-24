# Write a code combine both validations into a single program

import re

def validate_pan(pan):
    pattern = r'[A-Z]{5}[0-9]{4}[A-Z]{1}$'
    return bool(re.match(pattern, pan))

def validate_email(email):
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

pan = input("Enter PAN card number: ")
email = input("Enter Email ID: ")

print("\n--- Validation Results ---")

if validate_pan(pan):
    print("PAN Card: Valid")
else:
    print("PAN Card: Invalid")

if validate_email(email):
    print("Email ID: Valid")
else:
    print("Email ID: Invalid")
    