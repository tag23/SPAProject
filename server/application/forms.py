from flask_wtf import FlaskForm
from wtforms import StringField, DateField, PasswordField, validators, ValidationError
from wtforms.fields.html5 import EmailField
from wtforms.widgets import TextInput


def refresh_field(form, field):
    errors = ['Only latin characters', 'Password must match with confirmation field',
              'Field must be between 4 and 20 characters long.', 'Field must be between 4 and 25 characters long.',
              'This field is required.']
    if any(error in field.data for error in errors):
        raise ValidationError('clear')


def validate_only_latin_fields(form, field):
    if not all(ord(c) < 128 for c in field.data):
        raise ValidationError('Only latin characters')


class MyTextInput(TextInput):
    def __init__(self, error_class=u'has_errors'):
        super(MyTextInput, self).__init__()
        self.error_class = error_class

    def __call__(self, field, **kwargs):
        errors = ['Only latin characters', 'Password must match with confirmation field',
                  'This field requires a valid email address']
        print(field.errors)
        if 'clear' in field.errors:
            kwargs['value'] = ''

        for error in errors:
            if error in field.errors:
                c = kwargs.pop('class', '') or kwargs.pop('class_', '')
                kwargs['class'] = f'{self.error_class} {c}'
                kwargs['value'] = f'{error}'
        return super(MyTextInput, self).__call__(field, **kwargs)


class LoginForm(FlaskForm):
    user_login = EmailField('user_login',
                            widget=MyTextInput(), render_kw={"placeholder": "Email"})
    password = PasswordField('password',
                            widget=MyTextInput(), render_kw={"placeholder": "Password"})


class EditForm(FlaskForm):
    name = StringField('name', validators=[validators.Length(min=4, max=20), validators.DataRequired(),
                       validate_only_latin_fields])

    surname = StringField('surname', [validators.Length(min=4, max=20), validators.DataRequired(),
                                      validate_only_latin_fields])

    birthday_date = DateField('birthday_date', [validators.DataRequired()])


class RegistrationForm(FlaskForm):
    name = StringField('name', validators=[validators.Length(min=4, max=20), validators.DataRequired(),
                       validate_only_latin_fields, refresh_field], widget=MyTextInput(),
                       render_kw={"placeholder": "Name"})
    surname = StringField('surname', [validators.Length(min=4, max=20), validators.DataRequired(),
                       validate_only_latin_fields, refresh_field], widget=MyTextInput(),
                       render_kw={"placeholder": "Surname"})
    birthday_date = DateField('birthday_date', [validators.DataRequired()], widget=MyTextInput(),
                       render_kw={"placeholder": "Birthday"})
    user_login = EmailField('user_login', [validators.Length(min=4, max=25), validators.DataRequired(),
                       validators.Email("This field requires a valid email address")], widget=MyTextInput(),
                       render_kw={"placeholder": "Email"})
    password = PasswordField('password', [validators.Length(min=6, max=25), validators.DataRequired(),
                       validators.EqualTo('confirm', message='Password must match with confirmation field')],
                       widget=MyTextInput(), render_kw={"placeholder": "Password"})
    confirm = PasswordField('Repeat Password', [validators.DataRequired()], widget=MyTextInput(),
                       render_kw={"placeholder": "Confirm password"})
