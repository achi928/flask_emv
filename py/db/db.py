import psycopg2
from psycopg2 import Error

def connect():
  return psycopg2.connect(
    host = "localhost",
    port = 5432,
    database = "student",
    user = "postgres",
    password = "1928acchi"
  )
  
def close_resources(conn, cur):
  if cur is not None:
    try:
      cur.close()
    except Error as e:
      print(f"カーソルクローズ時にエラー: {e}")
  
  if conn is not None:
    try:
      conn.close()
    except Error as e:
      print(f"コネクションクローズ時にエラー: {e}")
  print("DB接続をクローズしました。")
  
  
def insert_user(name, age):
  conn = None
  cur = None
  try:
    conn = connect()
    cur = conn.cursor()
    cur.execute("insert into users (name, age) values (%s, %s)", (name, age))
    conn.commit()
    print("insertが完了しました。")
  except Error as e:
    if conn:
      conn.rollback()
    print(f"データ挿入中にエラーが発生しました: {e}")
  finally:
    close_resources(conn, cur)
    
    
def get_users():
  conn = None
  cur = None
  try:
    conn = connect()
    cur = conn.cursor()
    cur.execute("select id, name, age from users order by id")
    users = cur.fetchall()
    return users
  except Error as e:
    print(f"データ取得中にエラーが発生しました: {e}")
    return []
  finally:
    close_resources(conn, cur)
    

def update_user(user_id, new_name, new_age):
  conn = None
  cur = None
  try:
    conn = connect()
    cur = conn.cursor()
    cur.execute("update users set name = %s, age = %s where id = %s",
                (new_name, new_age, user_id))
    conn.commit()
    print("updateが完了しました。")
  except Error as e:
    if conn:
      conn.rollback()
    print(f"データ更新中にエラーが発生しました: {e}")
  finally:
    close_resources(conn, cur)
    
    
def delete_user(user_id):
  conn = None
  cur = None
  try:
    conn = connect()
    cur = conn.cursor()
    cur.execute("delete from users where id = %s", (user_id,))
    conn.commit()
    print("deletが完了しました。")
  except Error as e:
    if conn:
      conn.rollback()
    print(f"データ削除中にエラーが発生しました: {e}")
  finally:
    close_resources(conn, cur)


if __name__ == "__main__":
    # insert_user("Alice", 23)
    # insert_user("Bob", 31)
    
    print("登録されているユーザー一覧:")
    for user in get_users():
      print(user)
      
    update_user(1, "Alicia", 31)
    print("更新後:")
    for user in get_users():
      print(user)
      
    delete_user(1)
    print("削除後")
    for user in get_users():
      print(user)