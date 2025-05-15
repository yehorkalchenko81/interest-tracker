from flask import Flask, render_template

support_services = ('Instagram', 'Reddit')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', name='UserName', services=support_services)

@app.route('/about')
def about():
    return render_template('about.html', name='UserName')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)