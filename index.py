from flask import Flask, request, render_template
from classes.Person import *

app = Flask(__name__, template_folder='templates')
app.debug = True

@app.route('/', defaults={'user': 'World', 'id': 0})
@app.route('/<user>/', defaults={'id': 0})
@app.route('/<user>/<int:id>')
def hello(user, id):
	person = Person(user, id)
	return render_template('index.html', cred=person) 

if __name__ == '__main__':
	app.run()
