from flask import Flask, render_template, request
from utils import map

app=Flask(__name__)

'''put in html file nme'''

@app.route("/")
def root():
	return render_template("

if __name__ == '__main__':
	app.debug = True
	app.run()
