# エラー情報の通知

import smtplib  # メールを送信するための基本ライブラリ
from email.mime.text import MIMEText # メール内容を作成するためのライブラリ

def send_error_notification(subject, body):
  # メールの内容を設定
  msg = MIMEText(body)
  msg["subject"] = subject
  msg["From"] = "" # 送信元のメールアドレス
  msg["To"] = "" # 送信先のメールアドレス
  
  # SMTPサーバー（Mailpit）を利用してメールを送信
  # MailpitのデフォルトSMTPポートは1025
  with smtplib.SMTP("localhost", 1025) as server: # Javaのtry-with-resouecesと同じ
    server.send_message(msg)
    
# バッチ処理でエラーが発生した時に呼び出す
try:
  result = 10 / 0
except Exception as e:
  error_message = f"バッチ処理でエラーが発生しました: {e}"
  print(error_message)
  # メールで通知
  send_error_notification("バッチ処理エラー通知", error_message)