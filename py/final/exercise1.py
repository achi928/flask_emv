# apiとの通信を行う
import psycopg2
from psycopg2 import Error
# ログの出力
import logging


logging.basicConfig(
    filename="final_exercise.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def connect():
    return psycopg2.connect(
        host="localhost",
        port=5432,
        database="student",
        user="postgres",
        password="1928acchi"
    )

def close_resources(conn, cur):
    if cur is not None:
        try:
            cur.close()
        except Error as e:
            logging.error(f"カーソルクローズ時にエラー: {e}")
            print("loggingと、printの違いを調べる")
    if conn is not None:
        try:
            conn.close()
        except Error as e:
            logging.error(f"コネクションクローズ時にエラー: {e}")
    logging.info("DB接続をクローズしました。")
    print("DB接続をクローズしました。")


def insert_user(name, email, phone, website, company_name):
    conn = None
    cur = None
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO users (name, email, phone, website, company_name)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id;
        """, (name, email, phone, website, company_name))
        user_id = cur.fetchone()[0]
        conn.commit()
        msg = f"userを登録しました (id={user_id}, name={name})"
        print(msg)
        logging.info(msg)
        return user_id
    except Error as e:
        if conn:
            conn.rollback()
        logging.error(f"user登録中にエラー: {e}")
    finally:
        close_resources(conn, cur)


def insert_album(user_id, title):
    conn = None
    cur = None
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO albums (user_id, title)
            VALUES (%s, %s)
            RETURNING id;
        """, (user_id, title))
        album_id = cur.fetchone()[0]
        conn.commit()
        msg = f"albumを登録しました (id={album_id}, title={title}, user_id={user_id})"
        print(msg)
        logging.info(msg)
        return album_id
    except Error as e:
        if conn:
            conn.rollback()
        logging.error(f"album登録中にエラー: {e}")
    finally:
        close_resources(conn, cur)


def insert_photo(album_id, title, url, thumbnail_url):
    conn = None
    cur = None
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO photos (album_id, title, url, thumbnail_url)
            VALUES (%s, %s, %s, %s)
            RETURNING id;
        """, (album_id, title, url, thumbnail_url))
        photo_id = cur.fetchone()[0]
        conn.commit()
        msg = f"photoを登録しました (id={photo_id}, title={title}, album_id={album_id})"
        print(msg)
        logging.info(msg)
        return photo_id
    except Error as e:
        if conn:
            conn.rollback()
        logging.error(f"photo登録中にエラー: {e}")
    finally:
        close_resources(conn, cur)


if __name__ == "__main__":
    # 1. userを作成
    user_id = insert_user("あち", "achi@example.com", "123-456-789", "suru", "株式会社パイソン")

    # 2. albumを作成
    album_id = insert_album(user_id, "あちのアルバム")

    # 3. photoを作成
    photo_id = insert_photo(album_id, "あちの写真", "achi-url", "jpg")
