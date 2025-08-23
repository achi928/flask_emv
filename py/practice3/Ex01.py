import requests
import pandas as pd

output_file = "date/output_request.csv"

url = "https://jsonplaceholder.typicode.com/posts/1"
responce = requests.get(url)

result = responce.json()

df = pd.DataFrame([result])
df.to_csv(output_file)

