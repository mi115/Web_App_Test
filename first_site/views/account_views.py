import flask
from flask import redirect
from flask import url_for
from first_site.infrastructure.view_modifiers import response
import first_site.services.user_service as user_service
import first_site.infrastructure.cookie_auth as cookie_auth
from first_site.infrastructure import request_dict

blueprint = flask.Blueprint('account', __name__, template_folder='templates')

# ######################### INDEX #############################


@blueprint.route('/account')
@response(template_file='account/index.html')
def index():
    user_id = cookie_auth.get_user_id_via_auth_cookie(flask.request)
    if user_id is None:
        return flask.redirect('/account/login')
    user = user_service.find_user_by_id(user_id)
    if not user:
        return flask.redirect('/account/login')

    return {
        'user': user,
        'user_id': cookie_auth.get_user_id_via_auth_cookie(flask.request),
    }


# ######################### REGISTER #############################


@blueprint.route('/account/register', methods=['GET'])
@response(template_file='account/register.html')
def register_get():
    return {'user_id': cookie_auth.get_user_id_via_auth_cookie(flask.request),}


@blueprint.route('/account/register', methods=['POST'])
@response(template_file='account/register.html')
def register_post():
    r = flask.request

    name = r.form.get('name')
    email = r.form.get('email', '').lower().strip()
    password = r.form.get('password').strip()

    if not name or not email or not password:
        return {
            'name': name,
            'password': password,
            'email': email,
            'error': 'Some required fields are missing.'
        }

    # TODO: Create the user
    user = user_service.create_user(name, email, password)
    if not user:
        return {
            'name': name,
            'password': password,
            'email': email,
            'error': 'A user with that email already exists.'
        }

    resp = flask.redirect('/account')
    cookie_auth.set_auth(resp, user.id)

    return resp


# ######################### LOGIN #############################


@blueprint.route('/account/login', methods=['GET'])
@response(template_file='account/login.html')
def login_get():
    return {'user_id': cookie_auth.get_user_id_via_auth_cookie(flask.request),}


@blueprint.route('/account/login', methods=['POST'])
@response(template_file='account/login.html')
def login_post():
    data = request_dict.create()

    email = data.email.lower().strip()
    password = data.password.strip()

    if not email or not password:
        return {
            'password': password,
            'email': email,
            'error': 'Some required fields are missing.'
        }

    # TODO: Validate the user
    user = user_service.login_user(email, password)
    if not user:
        return {
            'password': password,
            'email': email,
            'error': 'The account does not exist or the password is wrong.'
        }
    resp = flask.redirect('/account')
    cookie_auth.set_auth(resp, user.id)

    return resp


# ######################### LOGOUT #############################


@blueprint.route('/account/logout')
def logout():
    resp = flask.redirect('/')
    cookie_auth.logout(resp)

    return resp