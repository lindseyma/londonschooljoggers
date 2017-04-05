from flask import Flask, render_template
from utils import data, drugs, labor

#import utils

schema = labor._guess_schema('a')

app = Flask(__name__)
app.secret_key="idkjustsomethingrandom"

@app.route('/')
def root():
	DrugList = data.makeDrugList()
	PainList = data.makePainList()
	AlcoholList = data.makeAlcoholList()
	return render_template('index.html')

if __name__ == '__main__':
	app.debug = True
	app.run()

