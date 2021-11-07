import os

# os.path.dirname를 두번 사용하는 이유
# 경로가 폴더 안에 들어오왔기 때문에 한번 더 앞으로 가야되기 때문
BASE_DIR = os.path.dirname(os.path.dirname(__file__))