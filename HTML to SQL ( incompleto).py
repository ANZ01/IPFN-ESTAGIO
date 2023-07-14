# app.py
import sqlite3
from flask import Flask, request, redirect, url_for, render_template
import bs4


conn = sqlite3.connect('vectrix.db')

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        # get all values from submitted form
        nome = request.form['NOME']
        email = request.form['EMAIL']
        password = request.form['PASSWORD']

        # do something with those variables.. e.g storing them in DB etc...
        print(f'Name:{nome}')

        print(f'email:{email}')

        print(f'password:{password}')
        #cursor=conn.cursor()
        #cursor.execute("INSERT INTO FORM(NOME,EMAIL,PASSWORD) VALUES(?,?,?);", ({nome},{email},{password}))
        #conn.commit()
       # conn.close()

        return redirect(url_for("submit_form"))
    else:
        # show form template
        return render_template("submit_form.html")


if __name__ == "__main__":
    app.run(port = 8000)