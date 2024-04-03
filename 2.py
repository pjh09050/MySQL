import pymysql

# 전역 변수 선언부
conn, cur = None, None
data1, data2, data3, data4 = "", "", "", ""
sql = ""

# 메인 코드
conn = pymysql.connect(host='localhost', user='root', password='0000', db='state', charset='utf8')
cur = conn.cursor()

while (True):
    data1 = input('사용자 ID ==> ')
    if data1 == "":
        break;
    data2 = input('사용자 이름 ==> ')
    data3 = input('사용자 이메일 ==> ')
    data4 = input('사용자 출생연도 ==> ')
    # INSERT INTO userTable VALUES('hong', '홍지윤', 'hong@naver.com', 1996)
    sql = "INSERT INTO userTable VALUES('" + data1 + "', '" + data2 + "', '" + data3 + "', '" + data4 + "')"
    cur.execute(sql)
    
conn.commit()
conn.close()