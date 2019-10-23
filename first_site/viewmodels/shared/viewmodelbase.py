import flask
from flask import Request
from first_site.infrastructure import request_dict


class ViewModelBase:
    def __init__(self):
        self.request: Request = flask.request
        self.request_dict = request_dict.
