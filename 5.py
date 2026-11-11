
import json
with open('token.json') as file:
    result = json.load(file)
print(type(result))
print(result['token'])
