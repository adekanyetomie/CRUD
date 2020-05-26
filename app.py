from flask import Flask,request, render_template, redirect, url_for, request
from toy import Toy
from flask_modus import Modus




app = Flask(__name__)
modus = Modus(app)


#@app.route('/')

#def hello():
   # return "Hello World!"

#@app.route('/welcome')
#def welcome():
 #   return "Wellcome"

#@app.route ('/<person>')  
#def name(person):
 #   return f"my name is {person}"

#CRUD EXAMPLE
lego = Toy(name = 'lego')
rubi = Toy(name = 'rubi')
cube = Toy(name = 'cube')

toys = [lego, rubi, cube]

@app.route('/toys', methods = ['GET', 'POST'],)
def index():
    if request.method == 'POST':
        toys.append(Toy(request.form['name']))
        return redirect(url_for('index'))     
    return render_template('index.html', toys=toys)

@app.route('/toys/new')
def new():
    return render_template('new.html')

@app.route('/toys/<int:id>' ,methods = ['GET', 'PATCH'])
def show(id):

    for toy in toys:
        if toy.id == id:    
            found_toy = toy

            if request.method == b'PATCH':
                found_toy.name = request.form['name']
                return redirect(url_for('index')) 
    return render_template ('show.html', toy= found_toy)

@app.route('/toys/<int:id>/edit')
def edit(id):
    # refactored found_toy in show() using a generator
    found_toy = next(toy for toy in toys if toy.id == id)
    return render_template('edit.html', toy = found_toy)

