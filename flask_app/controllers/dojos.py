from flask_app import app
from flask import render_template,request,redirect
from flask_app.models.dojo import Dojo


@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    all_dojos = Dojo.get_all()
    print(all_dojos)
    return render_template("dojo.html",all_dojos = all_dojos)

@app.route('/create/dojo',methods=["POST"])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/')

@app.route('/dojos/<int:id>')
def dojo_show(id):
    data ={
            'id': id
        }
    return render_template("dojoshow.html", show_dojo = Dojo.get_dojo_with_ninjas(data))