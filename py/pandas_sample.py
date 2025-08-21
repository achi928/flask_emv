import pandas as pd
from datetime import datetime

input_file = "date/input.csv"
output_file = "date/output.csv"

df = pd.read_csv(input_file)

total_sales = df["sales"].sum() # sales列の合計値を算出
average_sales = df["sales"].mean() # sales列の平均値を算出
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 新しいDateFrameを作成して出力
result_df = pd.DataFrame({
  "Total Sales" : [total_sales],
  "Average Sales" : [average_sales],
  "Timestamp" : [current_time]
})
result_df.to_csv(output_file, index=False)

print(f"ファイル処理が完了しました。合計値と平均値を出力しました。 実行時刻:{current_time}")