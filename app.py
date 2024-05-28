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

if __name__ == '__main__':
	app.run(debug=True)
