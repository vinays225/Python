import re

pan = "LTSDO8976G"
pattern = r'[A-Z]{5}[0-9]{4}[A-Z]'

# Use fullmatch if you want to validate entire PAN
if re.fullmatch(pattern, pan):
    print("Valid PAN")
else:
    print("Invalid PAN")
