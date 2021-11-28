# Python3 
import requests


print("Satria Tools! Get the header sites")
inp = input("sites : ")

r = requests.get(inp)

print(r.headers)
