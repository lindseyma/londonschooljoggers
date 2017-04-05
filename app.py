from flask import Flask, render_template
from utils import data, drugs, labor

#import utils

app = Flask(__name__)
app.secret_key="idkjustsomethingrandom"

@app.route('/')
def root():
        d = data.compileList()
        year = 2003
	return render_template('index.html',d=d, year=year)

if __name__ == '__main__':
	app.debug = True
	app.run()

