import os

BASE_DIR = os.path.dirname(__file__)

# SQLALCHEMY_DATABASE_URI는 데이터베이스 접속 주소
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
#SQLALCHEMY_TRACK_MODIFICATIONS는 SQLAlchemy의 이벤트를 처리하는 옵션이다. 이 옵션은 파이보에 필요하지 않으므로 False로 비활성화했다
SQLALCHEMY_TRACK_MODIFICATIONS = False