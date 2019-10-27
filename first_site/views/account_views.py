import email

import flask
from flask import redirect
from flask import url_for
from first_site.infrastructure.view_modifiers import response
import first_site.services.user_service as user_service
import first_site.infrastructure.cookie_auth as cookie_auth
from first_site.infrastructure import request_dict
from viewmodels.account.index_viewmodel import IndexViewModel
from viewmodels.account.login_viewmodel import LoginViewModel
from viewmodels.account.register_viewmodel import RegisterViewModel

blueprint = flask.Blueprint('account', __name__, template_folder='templates')

# ######################### INDEX #############################


@blueprint.route('/account')
@response(template_file='account/index.html')
def index():
    vm = IndexViewModel()
    if not vm.user:
        return flask.redirect('/account/login')
    return vm.to_dict()


# ######################### REGISTER #############################


@blueprint.route('/account/register', methods=['GET'])
@response(template_file='account/register.html')
def register_get():
    vm = RegisterViewModel()
    return vm.to_dict()


@blueprint.route('/account/register', methods=['POST'])
@response(template_file='account/register.html')
def register_post():
    vm = RegisterViewModel()
    vm.validate()
    if vm.error:
        return vm.to_dict()

    user = user_service.create_user(vm.name, vm.email, vm.password)
    if not user:
        vm.error = 'The account could not be created.'
        return vm.to_dict()

    resp = flask.redirect('/account')
    cookie_auth.set_auth(resp, user.id)
    return resp


# ######################### LOGIN #############################


@blueprint.route('/account/login', methods=['GET'])
@response(template_file='account/login.html')
def login_get():
    vm = LoginViewModel()
    return vm.to_dict()


@blueprint.route('/account/login', methods=['POST'])
@response(template_file='account/login.html')
def login_post():
    vm = LoginViewModel()
    vm.validate()
    if vm.error:
        return vm.to_dict()

    if not vm.user:
        vm.error = 'The account does not exist or the password is wrong.'
        return vm.to_dict()

    resp = flask.redirect('/account')
    cookie_auth.set_auth(resp, vm.user.id)

    return resp


# ######################### LOGOUT #############################


@blueprint.route('/account/logout')
def logout():
    resp = flask.redirect('/')
    cookie_auth.logout(resp)

    return resp