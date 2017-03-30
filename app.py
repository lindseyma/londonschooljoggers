from flask import Flask, render_template
from utils import map

app = Flask(__name___)
app.secret_key="idkjustsomethingrandom"

@app.route('/')
def root():
    return render_template('index.html')

if __name__ == '__main__':
	app.debug = True
	app.run()

