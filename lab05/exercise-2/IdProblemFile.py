print(f" ")
print("name ::Harika Neelam")
print(f"blazerId ::hneelam")
print(f" ")


import requests
import json

url = "https://michaelgathara.com/api/python-challenge"

response = requests.get(url)
challenges = response.json()
print(f" ")
print(challenges, end=" ")

print(f" ")

print(f" ")

for problem in challenges:
    Id = problem['id']
    expression = problem['problem'].replace('?', '')  
    
    try:
        result = eval(expression)
        print(f"Problem {Id} :: {expression} = {result}")
    except SyntaxError:
        print(f"Problem {Id} has an invalid expression :: {expression}")
