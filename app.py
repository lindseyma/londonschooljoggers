from flask import Flask, render_template
#from utils import map
import drugs
import labor

list_of_report = drugs.get_reports()
print list_of_report 

app = Flask(__name__)
app.secret_key="idkjustsomethingrandom"

@app.route('/')
def root():
	return render_template('index.html')

if __name__ == '__main__':
	app.debug = True
	app.run()

