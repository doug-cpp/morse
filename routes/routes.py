from flask import render_template, Blueprint, abort
from jinja2 import TemplateNotFound

morse_api = Blueprint('morse_api', __name__, template_folder='templates', static_folder='static')


@morse_api.route('/')
def morse_main():
    try:
        return render_template('index.html')
    except TemplateNotFound:
        abort(404)


def handle_error_routes(app):

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def page_not_found(e):
        return render_template('errors/500.html'), 500


