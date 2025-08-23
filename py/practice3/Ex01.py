import requests
import pandas as df

output_file = "date/output_request.csv"

url = "https://jsonplaceholder.typicode.com/posts/1"
responce = requests.get(url)

result = responce.json()
result.to_csv()

