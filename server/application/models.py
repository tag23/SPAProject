from werkzeug.security import generate_password_hash, check_password_hash

from . import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    surname = db.Column(db.String(20), unique=False, nullable=False)
    birthday_date = db.Column(db.Date, unique=False, nullable=False)
    user_login = db.Column(db.String(28), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)

    def __init__(self, name, surname, birthday_date, user_login, password):
        self.name = name
        self.surname = surname
        self.birthday_date = birthday_date
        self.user_login = user_login
        self.password = generate_password_hash(password, method='sha256')

    def __repr__(self):
        return f'<User {self.name}>'

    @classmethod
    def authenticate(cls, **kwargs):
        user_login = kwargs.get('user_login')
        password = kwargs.get('password')
        print(user_login, password)
        if not user_login or not password:
            return None

        user = cls.query.filter_by(user_login=user_login).first()
        print(check_password_hash(user.password, password))
        if not user or not check_password_hash(user.password, password):
            return None

        return user

    def to_dict(self):
        return dict(id=self.id,
                    name=self.name,
                    surname=self.surname,
                    birthday_date=self.birthday_date,
                    user_login=self.user_login,
                    password=self.password)
