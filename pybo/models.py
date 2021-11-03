from pybo import db

# 이때 db는 __init__.py 파일에서 생성한 SQLAlchemy 객체다
class Question(db.Model):
    #db.Colume 첫번째 인수는 데이터 타입
    # primary_key 고유 번호
    #데이터 타입이 db.Integer이고 기본키로 지정한 속성은 값이 자동으로 증가하는 특징도 있어서
    # 데이터를 저장할 때 해당 속성값을 지정하지 않아도 1씩 자동으로 증가하여 저장된다.
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # question_id 속성은 질문 모델과 연결하려고 추가했다.
    # 어떤 속성을 기존 모델과 연결하려면 db.ForeignKey를 사용해야 한다
    # 데이터베이스에서는 기존 모델과 연결된 속성을 외부 키(foreign key)라고 한다
    # db.ForeignKey에 지정한 첫 번째 값 'question.id'는 question 테이블의 id 컬럼을 의미한다.
    # Question 모델을 통해 테이블이 생성되면 테이블명은 question이 된다.
    # 두 번째 ondelete에 지정한 값은 삭제 연동 설정이다.
    # , 답변 모델의 question_id 속성은 질문 모델의 id 속성과 연결되며 ondelete='CASCADE'에 의해 데이터베이스에서 쿼리를 이용하여 질문을 삭제하면 해당 질문에 달린 답변도 함께 삭제된다.
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))

    # question 속성은 답변 모델에서 질문 모델을 참조하기 위해 추가했다
    #  예를 들어 답변 모델 객체에서 질문 모델 객체의 제목을 참조하려면 answer.question.subject처럼 할 수 있다
    # 이렇게 하려면 속성을 추가할 때 db.Column이 아닌 db.relationship을 사용해야 한다.
    # db.relationship에 지정한 첫 번째 값은 참조할 모델명이고 두 번째 backref에 지정한 값은 역참조 설정이다
    # 역참조란 쉽게 말해 질문에서 답변을 거꾸로 참조하는 것을 의미한다
    # 한 질문에는 여러 개의 답변이 달릴 수 있는데 역참조는 이 질문에 달린 답변을 참조할 수 있게 한
    #  예를 들어 어떤 질문에 해당하는 객체가 a_question이라면 a_question.answer_set와 같은 코드로 해당 질문에 달린 답변을 참조할 수 있다
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)