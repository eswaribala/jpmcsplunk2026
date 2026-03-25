import pymysql
import json
import time

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="vignesh",
    database="hospital_management_db"
)

cursor = conn.cursor(pymysql.cursors.DictCursor)

cursor.execute("SELECT * FROM person")

for row in cursor:
    print(json.dumps(row, default=str))   # Splunk reads stdout

cursor.close()
conn.close()