from flask import Flask, render_template
from utils import data

#import utils


app = Flask(__name__)
app.secret_key="idkjustsomethingrandom"

@app.route('/')
def root():
	DrugList = data.makeDrugList()
	PainList = data.makePainList()
	AlcoholList = data.makeAlcoholList()
        CompiledList = data.compileList()
	return render_template('index.html',compilelist=CompiledList)

if __name__ == '__main__':
	app.debug = True
	app.run()

