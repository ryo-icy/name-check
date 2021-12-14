import os
import socket

from dotenv import load_dotenv

load_dotenv()

IP = os.getenv('IP')
Domain = os.getenv('Domain')

res = socket.gethostbyname(Domain)
print(Domain, ':', res)
if IP != res:
    print(Domain, '!=', IP)
    exit(1)
