from flask import Flask, render_template, request, session
from utils import data, drugs, labor

#import utils

app = Flask(__name__)
app.secret_key="idkjustsomethingrandom"

@app.route('/', methods=["GET","POST"])
def root():
        if 'year' not in session :
                session['year'] = 0
                return render_template('index.html')
        d = data.compileList()
        l = data.makeLaborList()
        session['year'] = request.form['year']
        year = session['year']
        print year
        return render_template('index.html',d=d, year=year,l=l)

if __name__ == '__main__':
	app.debug = True
	app.run()

