from datetime import datetime, timedelta
from functools import wraps
from flask_wtf import CSRFProtect
import jwt as jwt
from flask import render_template, request, redirect, url_for, flash, jsonify, abort, make_response
from flask import current_app as app
from flask_cors import CORS, cross_origin

from server.application.forms import RegistrationForm, LoginForm, EditForm
from .models import db, User


CORS(app)

@app.route('/')
def index():
    return render_template('index.html')


def token_required(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        auth_headers = request.headers.get('Authorization', '').split()

        invalid_msg = {
            'message': 'Invalid token. Registeration and / or authentication required',
            'authenticated': False
        }
        expired_msg = {
            'message': 'Expired token. Reauthentication required.',
            'authenticated': False
        }

        if len(auth_headers) != 2:
            return jsonify(invalid_msg), 401

        try:
            token = auth_headers[1]
            data = jwt.decode(token, app.config['SECRET_KEY'])
            user = User.query.filter_by(user_login=data['sub']).first()
            if not user:
                raise RuntimeError('User not found')
            return f(user, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify(expired_msg), 401  # 401 is Unauthorized HTTP status code
        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            return jsonify(invalid_msg), 401

    return _verify


@app.route('/api/v1/get-users', methods=['GET'])
@token_required
def get_users(user):
    users = User.query.all()

    data = {
        'users': [user.to_dict() for user in users]
    }

    return jsonify({'data': data})


@app.route('/api/v1/get-user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if not user:
        abort(404)

    return jsonify({'user': user.to_dict()})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/api/v1/login', methods=['GET', 'POST'])
@cross_origin()
def login():
    form = LoginForm()
    if form.validate() and request.method == 'POST':
        data = request.get_json()
        user = User.authenticate(**data)

        if not user:
            return jsonify({'data': data, 'message': 'Invalid credentials', 'authenticated': False}), 401

        token = jwt.encode({
            'sub': user.user_login,
            'iat': datetime.utcnow(),
            'exp': datetime.utcnow() + timedelta(minutes=30)},
            app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('UTF-8')})

    return render_template('login.html', form=form)


@app.route('/api/v1/register', methods=['GET', 'POST'])
@cross_origin()
def register():
    form = RegistrationForm()
    user = None
    if form.validate() and request.method == 'POST':

        data = request.get_json()
        name = data['name']
        surname = data['surname']
        birthday = data['birthday_date']
        user_login = data['user_login']
        password = data['password']
        user = User(name, surname, birthday,
                    user_login, password)
        if user:
            db.session.add(user)
            db.session.commit()

    return jsonify(user.to_dict()), 201


#   return render_template('register.html', form=form)


@app.route('/api/v1/delete', methods=['GET'])
@cross_origin()
def delete():
    data = request.args.get('user_id')
    user = User.query.filter_by(id=data).first()
    if user:
        db.session.delete(user)
        db.session.commit()
    return jsonify()


@app.route('/api/v1/edit', methods=['GET', 'POST'])
@cross_origin()
def edit():
    form = EditForm()
    user = None
    if request.method == 'POST':

        data = request.get_json()
        print(data)
        name = data['data']['name']
        surname = data['data']['surname']
        birthday = data['data']['birthday_date']
        user = User.query.filter_by(id=data['data']['id']).first()
        print(user)
        if user:
            user.name = name
            user.surname = surname
            user.birthday_date = birthday
            db.session.commit()
            return jsonify(user.to_dict()), 201
    else:
        print('Error')
    return jsonify({'success': False})


@app.route('/users', methods=['GET', 'POST'])
def users():
    users = User.query.all()
    return render_template('user-list.html', users=users)


