import logging

logging.basicConfig(
  filename = "date/batch.log",
  level = logging.INFO,
  format="%(asctime)s [%(levelname)s] %(message)s"
)

def do_logging():
  logging.info("プログラムが開始されました")
  print("logging完了")

do_logging()