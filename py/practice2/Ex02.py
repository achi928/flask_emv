import pandas as pd
from datetime import datetime

input_file = "date/input1.csv"
output_file = "date/output1.csv"

df = pd.read_csv(input_file)

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
total_score = df["scores"].sum()
average_score = df["scores"].mean()

result_df = pd.DataFrame({
  "Timestamp" : [timestamp], "Total Score" : [total_score], "Average Score" : [average_score]
})
result_df.to_csv(output_file, index = False)

print(f"ファイル処理が完了しました。合計値と平均値を出力しました。 実行時刻:{timestamp}")