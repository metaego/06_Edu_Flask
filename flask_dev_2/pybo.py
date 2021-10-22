from flask import Flask

# 플라스크 애플리케이션을 생성하는 코드
app = Flask(__name__) # __name__이라는 변수에 모듈명이 담김
# 이 파일이 실행되면 pybo.py라는 모듈이 실행되므로 __name__에는 pybo라는 문자열이 담김


# @app.route: 특정 주소에 접속하면 바로 다음 줄에 있는 함수를 호출하는 플라스크의 데코레이터
@app.route('/')
def hello_pybo():
    return 'Hello pybo!'
# flak run 실행시 환경변수의 기본값이 설정되지 않았다면 오류발생
# set FLASK_APP=pybo 로 환경변수 기본값 설정
# set FLASK_ENV=development, 플라스크 서버를 개발 환경으로 실행