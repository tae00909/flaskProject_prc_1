from flask import Flask

# app = Flask(__name__)은 플라스크 애플리케이션을 생성하는 코드
# __name__이라는 변수에는 모듈명이 담긴다.
# 즉, 이 파일이 실행되면 app.py라는 모듈이 실행되는 것이므로 __name__ 변수에는 "app" 라는 문자열이 담긴다
app = Flask(__name__)

# @app.route는 특정 URL에 접속하면 바로 다음 줄에 있는 함수를 호출하는 플라스크의 데코레이터
@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
