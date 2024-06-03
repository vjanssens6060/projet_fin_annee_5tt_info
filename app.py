from flask import Flask, render_template, request, redirect, url_for
from flask import session
import csv
import fn_classement_F1 as fnht


app = Flask(__name__)
app.secret_key = b'bafe004cc8de79cc96482b95db2d75473a3aa855b3270350267ccc92bddd46c5'

@app.route('/', methods=['GET'])
@app.route("/index", methods=['GET'])
def index():    
    db_name = fnht.fn_get_db_name()
    data = fnht.fn_dict_team(db_name)
    return render_template('index.html', data=data)

@app.route("/encode_team", methods=['GET', 'POST'])
def encode_team():
    if request.method == 'GET':
        return render_template('encode_team.html')

    elif request.method == 'POST':
        session['nom'] = request.form['nom']
        session['directeur'] = request.form['directeur']
        session['position_classement_constructeur'] = request.form['position_classement_constructeur']        

        db_name = fnht.fn_get_db_name()                   
        fnht.set_team_data(db_name, team_data)
        
        return redirect('/index')


if __name__ == '__main__':
	app.run(debug=True)
