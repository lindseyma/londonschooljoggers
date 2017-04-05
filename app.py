from flask import Flask, render_template
from utils import data, drugs, labor

#import utils

app = Flask(__name__)
app.secret_key="idkjustsomethingrandom"

@app.route('/', methods=['GET'])
def root():
        d = data.compileList()
        l = data.makeLaborList()
        year = 2003
	return render_template('index.html',d=d, year=year,l=l)

if __name__ == '__main__':
	app.debug = True
	app.run()

