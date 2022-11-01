import requests

"""GET
req = requests.get(
    "https://teste-2fe9d-default-rtdb.firebaseio.com/.json")
print(req)
print(req.json())
"""

"""POST
info = '{"Nome": "Mariazinha"}'
req = requests.post(
    "https://teste-2fe9d-default-rtdb.firebaseio.com/.json", data=info)
print(req)
print(req.json())
"""

"""PATCH
info = '{"Nome": "Joca", "Idade": "39", "Sexo":"M"}'
req = requests.patch(
    "https://teste-2fe9d-default-rtdb.firebaseio.com/-NFU0RsWTzy6PhLBofru.json", data=info)
print(req)
print(req.json())
"""

"""DELETE
req = requests.delete(
    "https://teste-2fe9d-default-rtdb.firebaseio.com/-NFU0_SMOz7-v2oTO923.json")
print(req)
print(req.json())
"""
