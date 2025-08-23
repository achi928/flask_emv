import pandas as pd
import logging

logging.basicConfig(
  filename = "date/batch2.log",
  level = logging.INFO,
  format = "%(asctime)s [%(levelname)s] %(message)s"
)

input_file = "date/input2.csv"
outpuut_file = "date/output2.csv"

try:
  logging.info("処理開始")

  df = pd.read_csv(input_file)

  average_score = df.groupby("date", as_index = False)["score"].mean()
  average_score.colums = ["Date", "Average Score"]

  average_score.to_csv("date/output2.csv")
  logging.info("各日の平均スコア出力しました。")

except FileNotFoundError as e:
  logging.error(f"{input_file} の読み込みに失敗しました: {e}")
  logging.info("エラー!!")
  print("エラー!!")