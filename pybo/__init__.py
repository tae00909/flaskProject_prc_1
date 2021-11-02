from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

# db. migrate 객체 생성
db = SQLAlchemy()
migrate = Migrate()

# create_app은 애플리케이션 팩토리다.
# 애플리케이션 팩토리란 쉽게 말해 app 객체를 생성하는 함수를 의미
# create_app 함수를 다른 이름으로 했을 경우 에러가 날 것이다.
# 왜냐하면 create_app는 플라스크 내부에서 정의한 함수명이다
def create_app():
    # app = Flask(__name__)은 플라스크 애플리케이션을 생성하는 코드
    # __name__이라는 변수에는 모듈명이 담긴다.
    # 즉, 이 파일이 실행되면 app.py라는 모듈이 실행되는 것이므로 __name__ 변수에는 "app" 라는 문자열이 담긴다
    app = Flask(__name__)

    # config.py 파일에 작성한 항목을 app.config 환경변수로 부리기 위해
    app.config.from_object(config)

    # ORM
    # db, migrate를 init_app 메서드를 이용해 초기화
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models


    # # print(__name__) -> pybo 출력
    # # @app.route는 특정 URL에 접속하면 바로 다음 줄에 있는 함수를 호출하는 플라스크의 데코레이터
    # @app.route('/')
    # def hello_pybo():
    #     return 'Hello, pybo!'

    # 블루 프린트
    from .views import main_views
    # 블루 프린트를 사용하도록 변경
    app.register_blueprint(main_views.bp)

    return app



# if __name__ == '__main__':
#     app.run()
