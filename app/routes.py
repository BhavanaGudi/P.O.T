from flask import render_template, request
from app import app

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('start.html', title='Home')
    elif request.method == 'POST':
        userType = request.form['type']
        if (userType == "teacher"):
            return redirect(url_for('teacherLogin'))
        elif (userType == "student"):
            return redirect(url_for('studentLogin'))


@app.route('/teacherLogin', methods=['GET', 'POST'])
def teacherLogin():
    if request.method == 'GET':
        return render_template('teacherLogin.html', title='Teacher')

@app.route('/studentLogin', methods=['GET', 'POST'])
def studentLogin():
    if request.method == 'GET':
        return render_template('studentLogin.html', title='Student')

@app.route('/admin', methods=['GET', 'POST'])
def adminLogin():
    if request.method == 'GET':
        return render_template('adminLogin.html', title='Student')


