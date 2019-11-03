import flask

import first_site.infrastructure.cookie_auth as cookie_auth
from first_site.infrastructure.view_modifiers import response
from first_site.services import package_service
from first_site.services import user_service

blueprint = flask.Blueprint('home', __name__, template_folder='templates')


@blueprint.route('/')
@response(template_file="home/index.html")
def index():
    return {
        'releases': package_service.get_latest_releases(),
        'package_count': package_service.get_package_count(),
        'release_count': package_service.get_release_count(),
        'user_count': user_service.get_user_count(),
        'user_id': cookie_auth.get_user_id_via_auth_cookie(flask.request),
    }


@blueprint.route('/about')
@response(template_file='home/about.html')
def about():
    return {'user_id': cookie_auth.get_user_id_via_auth_cookie(flask.request),}
