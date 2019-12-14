from flask import Flask, send_from_directory, render_template, request, flash, redirect, session, jsonify

from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, User

from jinja2 import StrictUndefined


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "123"


@app.route("/")
def index():
    """Show homepage."""

    return render_template("index.html")

@app.route("/login-process")
def login_process():
    





# if running this file
if __name__ == "__main__":
    # connect app to db
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)