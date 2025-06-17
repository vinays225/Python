import re

email = "vinay.kumar@openai.com"
pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,3}$'

if re.fullmatch(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")
