from flask import render_template, Blueprint


morse_api = Blueprint('morse_api', __name__)


@morse_api.route('/')
def morse_main():
    return render_template('index.html')


@morse_api.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404


@morse_api.errorhandler(500)
def page_not_found(e):
    return render_template('errors/500.html'), 500

