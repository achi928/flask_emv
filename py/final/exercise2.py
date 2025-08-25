import psycopg2
import pandas as pd
from datetime import datetime
import logging

logging.basicConfig(
    filename="final_exercise.log",
    level=logging.INFO,
    format="%(asctime)s, [%(levelname)s] %(message)s"
)

def connect():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        database="student",
        user="postgres",
        password="1928acchi"
    )

def export_report():
    conn = None
    cur = None
    try:
        logging.info("DB登録を開始しました。")
        conn = connect()
        cur = conn.cursor()

        query = """
        SELECT
            u.id AS user_id,
            ua.total_albums,
            a.id AS album_id,
            pa.total_photos
        FROM users u
        JOIN (
            SELECT user_id, COUNT(*) AS total_albums
            FROM albums
            GROUP BY user_id
        ) ua ON u.id = ua.user_id
        JOIN albums a ON u.id = a.user_id
        JOIN (
            SELECT album_id, COUNT(*) AS total_photos
            FROM photos
            GROUP BY album_id
        ) pa ON a.id = pa.album_id
        ORDER BY u.id, a.id;
        """
        cur.execute(query)
        rows = cur.fetchall()

        df = pd.DataFrame(rows, columns=["user_id", "user_total_albums", "album_id", "album_total_photos"])

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        df.to_csv("final_exercise.csv", index=False)

        logging.info("DB登録が完了しました。")
        print(f"ファイル処理が完了しました。 実行時刻:{current_time}")

    except Exception as e:
        logging.error(f"エラーが発生しました: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
        logging.info("DB接続をクローズしました。")

if __name__ == "__main__":
    export_report()
