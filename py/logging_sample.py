import logging

logging.basicConfig(
  filename = "date/sample.log", #ログの出力先ファイルを指定
  level = logging.INFO, #ログレベルをINFOに設定
  format = "%(asctime)s [%(levelname)s] %(message)s" #ログのフォーマット指定
)

logging.info("プログラムが開始されました")
try:
  result = 10 / 2
  logging.info(f"計算結果: {result}")
except ZeroDivisionError:
  logging.error("ゼロ除算エラーが発生しました")
finally:
  logging.info("プログラムが終了しました")