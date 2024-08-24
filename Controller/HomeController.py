from flask import Blueprint, render_template, request, redirect, url_for, flash
from Forms.forms import LoginForm, BreakForm
import requests

# Define the Controller blueprint
home_bp = Blueprint('home_bp', __name__)

@home_bp.route('/', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data
        
        # Send data to the login API endpoint
        api_url = 'http://127.0.0.1:5000/api/login'
        response = requests.post(api_url, json={'username': username, 'password': password})
        
        if response.status_code == 200:
            flash('Login successful!', 'success')
            return redirect(url_for('home_bp.welcome'))  # Redirect to a dashboard or home page
        else:
            flash('Invalid username or password.', 'danger')
    
    return render_template('login.html', login_form=login_form)



@home_bp.route('/break', methods=['GET', 'POST'])
def welcome():
    form = BreakForm()
    login_form = LoginForm()
    if form.validate_on_submit():
        # Handle the "Take Break" action
        flash('Thanks for clocking in! Logging you out in 5 seconds...', 'success')
        # Render the page with the redirect flag
        return render_template('login.html', login_form=login_form, redirect_to_login=True)

    return render_template('break.html', form=form, redirect_to_login=False)