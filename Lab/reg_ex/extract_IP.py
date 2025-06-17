import re
text = "Server IPs: 192.168.1.1 and 10.0.0.254"
pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
print(re.findall(pattern, text))  # ['192.168.1.1', '10.0.0.254']