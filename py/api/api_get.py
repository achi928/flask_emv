import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

# APIから取得したJSONデータを取得
print(response.json()) 
