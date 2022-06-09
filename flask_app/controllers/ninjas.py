from flask_app import app
from flask import render_template, request, redirect
from flask_app.models import dojo, ninja


@app.route('/ninjas')
def ninjas():
    return render_template ("ninja.html",all_dojos=dojo.Dojo.get_all())

@app.route('/create/ninja', methods=["POST"])
def create_ninja():
    data = {
        "dojo_id": request.form['dojo_id'],
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "age" : request.form['age']
    }
    print(request.form)
    ninja.Ninja.save(data)
    return redirect ('/')