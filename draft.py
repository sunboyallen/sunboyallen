import numpy as np

import requests

url = 'http://httpbin.org/get?name=germey&age=22'

response = requests.get(url)

# print(response.json())
print(response.text)

# print(np.__version__)
