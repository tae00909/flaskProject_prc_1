from flask import Blueprint, url_for
from werkzeug.utils import redirect

# 블루 프린트
# 'main'(이름), __name__(모듈명), url_prefix='/'(URL 프리픽스)
# URL 프리픽스는 특정 파일(main_views.py)에 있는 함수의 애너테이션 URL 앞에 기본으로 붙일 접두어 URL을 의미한다.
# 예를 들어 main_views.py 파일의 URL 프리픽스에 url_prefix='/' 대신 url_prefix='/main'이라고 입력했다면
# hello_pybo 함수를 호출하는 URL은 localhost:5000/이 아니라 localhost:5000/main/이 된다
bp = Blueprint('main', __name__, url_prefix='/')

# app.route -> bp.route
@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    return redirect(url_for('question._list'))