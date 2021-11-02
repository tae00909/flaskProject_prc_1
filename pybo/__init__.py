from flask import Flask

# create_app은 애플리케이션 팩토리다.
# 애플리케이션 팩토리란 쉽게 말해 app 객체를 생성하는 함수를 의미
# create_app 함수를 다른 이름으로 했을 경우 에러가 날 것이다.
# 왜냐하면 create_app는 플라스크 내부에서 정의한 함수명이다
def create_app():
    # app = Flask(__name__)은 플라스크 애플리케이션을 생성하는 코드
    # __name__이라는 변수에는 모듈명이 담긴다.
    # 즉, 이 파일이 실행되면 app.py라는 모듈이 실행되는 것이므로 __name__ 변수에는 "app" 라는 문자열이 담긴다
    app = Flask(__name__)
    # print(__name__) -> pybo 출력
    # @app.route는 특정 URL에 접속하면 바로 다음 줄에 있는 함수를 호출하는 플라스크의 데코레이터
    @app.route('/')
    def hello_pybo():
        return 'Hello, pybo!'

    return app



# if __name__ == '__main__':
#     app.run()
