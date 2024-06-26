from flask import flask
from views import views

app = flask(__name__)
app.register_blueprint(views, url_prefix="/")


if __name__ == '__main__':
    app.run(debug=True, port=8000)
