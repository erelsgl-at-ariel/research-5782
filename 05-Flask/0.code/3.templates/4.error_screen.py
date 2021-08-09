from flask import Flask, render_template
app = Flask(__name__)

users = [
    {'name': 'Joee Javany',
    'email': 'joo@example.com',
    'phone': '111-1111'},
    {'name': 'Tom Pythonovitch',
    'email': 'python_is_coool@example.com',
    'phone': '222-2222'},
]

@app.route('/')
def hello():
    return render_template('dynamic-layou.html' , users = users)

if __name__ == '__main__':
    app.run(debug = True)