from sqlalchemy import create_engine, Column, String, Integer, CHAR, text, Index, BIGINT, VARCHAR
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session

host = 'localhost'
port = '3306'
user = 'root'
password = '0000'
database = 'state'
charset = 'utf8'

# Create MySQL connection string
df_url = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset={charset}'
engine = create_engine(df_url, pool_size=20, pool_recycle=500, max_overflow=20)
"""
    pool_size : 연결할 수 있는 connection의 크기 지정
    pool_recycle : 주어진 초 이후에 다시 connection(재사용) --> mysql에서는 일정 시간 동안 connection이 없을 경우, 끊어버림.(mysql의 wait_timeout시간보다는 작아야함)
    max_overflow : 허용된 connection 수, 최대 얼마까지 허용할 것인지 (pool_size를 적절히 설정하여 과도한 연결을 방지하고, 혹시 모르는 일을 대비해 max_overflow를 설정하는 것)
"""

# 데이터베이스 삭제
# with engine.connect() as conn:
#     conn.execute(text(f'DROP DATABASE IF EXISTS {database}'))
# 데이터베이스 생성
# with engine.connect() as conn:
#     conn.execute(text(f'CREATE DATABASE IF NOT EXISTS {database}'))

# 테이블 정의
Base = declarative_base()
class User(Base):
    __tablename__='usertable'
    JOB = Column(CHAR(10), primary_key=True, unique=True, autoincrement=False)
    M1 = Column(BIGINT, nullable=False)
    M2 = Column(BIGINT, nullable=False)

Base.metadata.create_all(engine) # 스키마 생성
#Base.metadata.drop_all(engine) # 스키마 제거

# Session 생성 - sessionmaker
"""
    scoped_session : 같은 객체의 session을 만들어줌, 동일한 thread에서의 충돌방지를 위해 많이 사용함, 동일한 session에서 다른 작업을 해야할 경우 파라미터를 주고받을 수 있음
"""
Session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
session = Session()

# 데이터 추가
new_1 = User(JOB='J0101', M1=7, M2=3)
new_2 = User(JOB='J0102', M1=0, M2=10)
#session.add(new_1)
#session.add(new_2)

# 한 번에 데이터 여러개 추가
#session.add_all([User(JOB='J0103', M1=7, M2=3), User(JOB='J0104', M1=7, M2=3), User(JOB='J0105', M1=7, M2=3)])

# 데이터 수정 
# user_to_update = session.query(User).filter_by(JOB='J0101').first()
# if user_to_update:
#     user_to_update.M1 = 10
#     user_to_update.M2 = 5
#     session.commit()

# table에서 원하는 데이터 불러오기
# info = session.query(User).filter(User.JOB.in_(['J0101', 'J0104'])).all()
# for user in info:
#     print(f"JOB: {user.JOB}, M1: {user.M1}, M2: {user.M2}")
# 정보 모두 불러오기
# info = session.query(User, User.JOB).all()
# for user in info:
#     print(f"JOB: {user.JOB}")

# table에 있는 데이터 삭제
# session.query(User).filter(User.JOB=='J0105').delete()

# 커밋 후 종료
session.commit()
session.close()