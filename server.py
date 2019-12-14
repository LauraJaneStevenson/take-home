from flask import Flask, send_from_directory, render_template, request, flash, redirect, session, jsonify

from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, User, Lst, Task

from jinja2 import StrictUndefined


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "123"


@app.route("/")
def index():
    """Show homepage."""

    return render_template("homepage.html")

@app.route("/login-process", methods=['POST'])
def login_process():
    """Log in as user"""

    username = request.form["username"]
    password = request.form["password"]

    # query for user
    user = User.query.filter_by(username=username,password=password).first()


    # add user_id to the session 
    session["user_id"] = user.user_id
    session["username"] = user.username
    session["list_id"] = user.list_id

    return redirect("/list")


@app.route("/register")
def register():
    """Show registration page"""

    return render_template("register.html")

@app.route("/registration-process", methods=['POST'])
def register_user():
    """Add a user to the database."""
    
    # get info from form
    username = request.form["username"]
    password = request.form["password"]

    # get all existing usernames
    existing_usernames = db.session.query(User.username).all()
    
    # check if username from form is already taken
    for existing_username in existing_usernames:
        
        if username == existing_username[0]:

            return redirect("/register")

    # create the user's list
    new_list = Lst()
    db.session.add(new_list)
    db.session.commit()

    # if username not taken create new user object
    new_user = User(username=username, password=password,
                                       list_id=new_list.lst_id)
    db.session.add(new_user)
    db.session.commit()

    return redirect("/")


@app.route("/list")
def show_list():
    """Show to do list"""
    todos = Task.query.filter_by(lst_id=session["list_id"]).all()

    return render_template("list.html",todos=todos)

@app.route("/add-task",methods=['POST'])
def add_task():
    """Adds task to db"""

    new_task = Task(lst_id=session["list_id"],task_str=request.form["task"])
    db.session.add(new_task)
    db.session.commit()

    return redirect("/list")

@app.route("/all_tasks.json")
def all_tasks():
    """Returns a list of tasks from database"""

    # query all tasks with session's list id 
    tasks = Task.query.filter_by(lst_id=session["list_id"]).all()

    task_lst = []

    for t in tasks:
        task = {}
        task["id"] = t.task_id
        task["list_id"] = t.lst_id
        task["task_str"] = t.task_str

        task_lst.append(task)

    return jsonify(task_lst)

@app.route("/complete_task")
def complete_task():

    pass



# if running this file
if __name__ == "__main__":
    # connect app to db
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)