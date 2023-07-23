from flask import Flask, render_template, request, redirect,url_for,session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'  
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    

@app.route('/', methods=['GET'])
def index():
    return render_template('signin.html')


@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        firstname = request.form['firstname']
        lastname = request.form['lastname']


        existing_user = User.query.filter_by(email=email).first()
        
        has_uppercase = any(char.isupper() for char in password)
        has_lowercase = any(char.islower() for char in password)
        ends_with_number = password[-1].isdigit()
        length_check = len(password) >= 8
        passed_requirements = has_uppercase and has_lowercase and ends_with_number and length_check

        if passed_requirements:
            
            existing_user = User.query.filter_by(email=email).first()
            if existing_user:
               return render_template('alreadyinuse.html')
            else:
               user = User(email=email, password=password, firstname=firstname, lastname=lastname)
               db.session.add(user)
               db.session.commit()
               return redirect(url_for('thank_you'))
        else:
            return render_template('report.html', passed_requirements=passed_requirements,
                                   has_uppercase=has_uppercase, has_lowercase=has_lowercase,
                                   ends_with_number=ends_with_number, length_check=length_check) 

    return render_template('signup.html')

@app.route('/users', methods=['GET'])
def show_users():
    users = User.query.all()
    return render_template('users.html', users=users)

@app.route('/thankyou')
def thank_you():
    return render_template('thankyou.html')

@app.route('/invalid')
def invalid():
    return render_template('invalid.html')



@app.route('/signin', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(email=username).first()

        if user is not None and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('secret'))
        else:
            return redirect(url_for('invalid')) 

    return render_template('signin.html')


@app.route('/secret')
def secret():
    return render_template('secret.html')



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
