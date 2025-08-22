import requests

# タイムアウトの設定
url = "https://jsonplaceholder.typicode.com/posts/1"

try:
  response = requests.get(url, timeout = 5) # 5秒待って応答がなければエラー
  response.raise_for_status() # HTTPエラーがあれば例外を発生させる
  print(response.json())
except requests.Timeout:
  print("リクエストがタイムアウトしました")
except requests.RequestException as e:
  print(f"リクエストエラー: {e}")
  
  
# HTTPエラーの処理
url = "https://jsonplaceholder.typicode.com/posts/9999" # 存在しないデータ

response = requests.get(url)

if response.status_code == 404:
  print("データが見つかりません")
elif response.status_code == 500:
  print("サーバーエラーが発生しました")
else:
  print(response.json())
