from flask import Flask, render_template

app = Flask(__name___)
app.secret_key="idkjustsomethingrandom"

@app.route('/')
def root():
    return render_template('index.html')
