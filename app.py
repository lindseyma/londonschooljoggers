from flask import Flask, render_template
from utils import data



app = Flask(__name__)
app.secret_key="idkjustsomethingrandom"

@app.route('/')
def root():
	DrugList = makeDrugList()
	PainList = makePainList()
	AlcoholList = makeAlcoholList()
	return render_template('index.html')

if __name__ == '__main__':
	app.debug = True
	app.run()

