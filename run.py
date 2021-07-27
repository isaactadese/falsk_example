from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signin')
def signin():
    return render_template('signin.html')

@app.route('/thank_you')
def thank_you():
    exampleInputEmail1=request.args.get('exampleInputEmail1')
    return render_template('thank_you.html',exampleInputEmail1=exampleInputEmail1)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

if __name__ == '__main__':
    app.run()



##name of env
##activate myapp
##for install packge
##  cd C:\Windows.old\Users\finiti\AppData\Local\Programs\Python\Python38\Scripts