from flask import Flask, render_template, request, redirect, url_for
from flask import session
import csv
import fn_classement_F1 as fnht
import os
import sqlite3

def fn_get_db_name():
    file_path = os.path.realpath(__file__)
    work_dir = os.path.dirname(file_path)
    db_name = f'{work_dir}/data.db'
    return db_name

def fn_read_db(db_name, table_name):
    sqliteConnection = None
    try:            
        with sqlite3.connect(db_name, timeout=10) as sqliteConnection:
            print(f"Connected to the database {db_name}")
            cursor = sqliteConnection.cursor()                       
            try:
                if table_name == 'team':        
                    cursor.execute(f"SELECT * FROM TEAM;")
                    data = cursor.fetchall()
                    print("SQLite script executed successfully")
                    print(f'\nExecution du SELECT :')
                    for line in data:
                        print(line)
                    print()
            except sqlite3.Error as error:
                print(f"Error while executing SQLite script: {error}")
            finally:
                cursor.close()
    except sqlite3.Error as error:
        print(f"Error while connecting to SQLite: {error}")
    except Exception as error:
        print(f"{error}")
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")
            return data
        

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
        team_data = [session['nom'],session['directeur'],session['position_classement_constructeur']]
        fnht.fn_set_team_data(db_name, team_data)
        
        return redirect('/index')

@app.route("/edit_team/<id>", methods=['GET', 'POST'])
def edit_team(id):
    if request.method == 'GET':
        line = []
        db_name = fn_get_db_name()
        data = fnht.fn_dict_team_one_row(db_name, id)
        nom = data['nom']
        directeur =  data['directeur']
        position_classement_constructeur = data['position_classement_constructeur']

        return render_template('edit_team.html',
                                nom = nom,
                                directeur = directeur,
                                position_classement_constructeur = position_classement_constructeur
                                )
     
    elif request.method == 'POST':
        session['nom'] = request.form['nom']
        session['directeur'] = request.form['directeur']
        session['position_classement_constructeur'] = request.form['position_classement_constructeur']

        # Réécrire le fichier CSV avec les modifications
        db_name = fnht.fn_get_db_name() 
        team_data = [session['nom'],session['directeur'],session['position_classement_constructeur']]
        fnht.fn_update_team(team_data, id, db_name)
        
        return redirect('/index')


if __name__ == '__main__':
	app.run(debug=True)
