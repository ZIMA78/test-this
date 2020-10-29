import os
from bottle import route, run, static_file, view, redirect, request
from db import TodoItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///tasks.db")
Session = sessionmaker(bind=engine)
s = Session()


@route("/static/<filename:path>")
def send_static(filename):
    return static_file(filename, root="static")
a = {"dict": ""}


@route("/")
@view("index")
def index():
    total_tasks = s.query(TodoItem).count()
    incomplete = s.query(TodoItem).filter(TodoItem.is_completed == True).count()
    tasks = s.query(TodoItem).order_by(TodoItem.uid)
    return {"tasks": tasks, "total_tasks": total_tasks, "incomplete": incomplete, "f": a.values()}


@route("/api/delete/<uid:int>")
def api_delete(uid):
    s.query(TodoItem).filter(TodoItem.uid == uid).delete()
    s.commit()
    return redirect("/")


@route("/api/complete/<uid:int>")
def api_complete(uid):
    t = s.query(TodoItem).filter(TodoItem.uid == uid).first()
    t.is_completed = True
    s.commit()
    return "Ok"

@route("/add-task", method="POST")
def add_task():
    incomplete = s.query(TodoItem).filter(TodoItem.is_completed == False).count()
    desc = request.POST.description.strip()
    if incomplete < 10:
        if len(desc) > 0:
            t = TodoItem(desc)
            s.add(t)
            s.commit()
    else:
        a.pop("dict")
        a["dict"] = "Ты ленивое чмо" 

    return redirect("/")



###
if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080, debug=True)
