from rpgdiceroller import rolld, rollad, rolldis, rollmod, rolladmod, rolldismod
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

        if advantage and not disadvantage:
            if (mod!=0):
                result = rolladmod(faces, mod)
            else:
                result = rollad(faces)
        elif disadvantage and not advantage:
            if (mod!=0):
                result = rolldismod(faces, mod)
            else:
                result = rolldis(faces)
        elif (mod!=0):
            result = rollmod(faces, mod)
        else:
            result = rolld(faces)

        redirect(request.referrer)

    return render_template('index.html', result = result)
