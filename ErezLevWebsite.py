from flask import Flask, render_template

flask_app = Flask(__name__, template_folder="templates", static_folder="static")


@flask_app.route('/')
def home():
    return render_template("home.html")


@flask_app.route('/projects/')
def projects():
    return render_template("projects.html")


if __name__ == '__main__':
    flask_app.run(debug=True)
