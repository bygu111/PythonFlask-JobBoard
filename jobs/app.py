from flask import Flask, render_template

app = Flask(__name__)

@raute()
def jobs():
    return render_template('index.html')