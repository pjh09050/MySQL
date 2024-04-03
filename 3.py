import pymysql

# 전역 변수 선언부
conn, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
row = ""  # 행을 하나씩 읽어오기 위해 row를 설정

# 메인 코드
conn = pymysql.connect(host='localhost', user='root', password='0000', db='state', charset='utf8')
cur = conn.cursor()

cur.execute("SELECT * FROM userTable")
print('사용자ID    사용자이름    이메일    출생연도')
print('---------------------------------------------')

while (True):
    row = cur.fetchone()
    if row==None:
        break
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    print("%5s   %15s   %20s   %d"%(data1, data2, data3, data4))

conn.close()