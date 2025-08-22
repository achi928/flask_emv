import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
update_date = {
  "title" : "Updated Title",
  "body" : "更新した内容をここに記載します",
  "userId" : 1
}

response = requests.put(url, json = update_date)

print(response.json())