import requests

url = "https://jsonplaceholder.typicode.com/posts"
data = {
  "title": "Python API Test",
  "body" : "これはテスト投稿です",
  "userId" : 1
}

# data変数をjson形式に変換し、リクエストを送信
response = requests.post(url, json = data)

# APIから取得したJSONデータを取得
print(response.json())
