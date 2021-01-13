from rpgdiceroller import rolld, rollad, rolldis, rollmod
from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

@app.route('/', methods=('GET', 'POST'))
def index():
    result = 0
    
    if request.method == 'POST':
        faces = int(request.form['faces'])
        if request.form['mod']:
            mod = int(request.form['mod'])
        else:
            mod = 0
        advantage = request.form.get('advantage')
        disadvantage = request.form.get('disadvantage')
        if (mod==0):
            if advantage and not disadvantage:
                result = rollad(faces)
            elif disadvantage and not advantage:
                result = rolldis(faces)
            else:
                result = rolld(faces)
        else:
            result = rollmod(faces, mod)

        redirect(request.referrer)
        
    return render_template('index.html', result = result)