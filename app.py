import email
from flask import Flask, render_template, request, redirect, url_for, session
from constants import FLASK_APP_DB

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

users = FLASK_APP_DB ['users'] #User collection

@app.route("/")

def home():
    if 'email' in session:
     return render_template("index.html")
    else:
        return redirect (url_for('signin'))


@app.route("/about")
def about():
    return render_template("about.html")    

@app.route("/signup", methods=['GET','POST'])
def signup():
    if request.method == 'GET' :
      return render_template ( "signup.html" )
    elif request.method == 'POST':
      first_name = request.form.get ('first_name')
      last_name = request.form.get ('last_name')
      email = request.form.get ('email')
      password = request.form.get ('password')
    

    data= users.find_one ({"first_name": 'first_name'})
    if data:
        return render_template("signup.html", warning=True)
    else:
     users.insert_one ({
        "first_name":first_name,
        "lastname": last_name,
        "email": email,
        "password" : password,
     })
    return redirect (url_for('signin'))
@app.route("/signin", methods=['GET','POST'])
def signin():
    if request.method == 'GET':
     return render_template('signin.html')
    elif request.method == 'POST': 
        email = request.form.get('email')
        password = request.form.get('password')

    user_exits = users.find_one({"email" : email})

    if user_exits:
        print("i am here")

        if user_exits ['password'] == password:
            session['email'] = email
            return redirect (url_for('home'))
        else:
            return render_template('signin.html', invalid_pas=True)
    else:
         return render_template('signin.html', invalid_cred=True)
     
    return render_template('signin.html')

@app.route('/logout')
def logout():
    session.pop('email', None)
    return render_template('signin.html')

if __name__ == '__main__':
  app.run(debug=True)