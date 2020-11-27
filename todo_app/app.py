from flask import Flask, render_template, request, redirect

import todo_app.data.session_items as session_items
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    items = session_items.get_items()

    return render_template("index.html", items=items)


@app.route('/add', methods = ["POST"])
def add_todo():
    title = request.form["title"]
    session_items.add_item(title)
    return redirect("/")

if __name__ == '__main__':
    app.run()
