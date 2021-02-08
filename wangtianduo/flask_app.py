from flask import Flask,request,render_template,redirect
import json

app = Flask(__name__)

term5coh1 = [{
'mon': {'0':'50.034', '1':'50.034', '2':'50.034', '3':'50.005', 
        '4':'50.005', '5':'50.005', '6':'50.003', '7':'50.003',
        '8':'50.003', '9':'null', '10':'null', '11':'null',
        '12':'null', '13':'hass', '14':'hass', '15':'hass',
        '16':'hass', '17':'hass', '18':'hass'}, 
'tue': {'0':'hass', '1':'hass', '2':'hass', '3':'null', 
        '4':'null', '5':'null', '6':'50.034', '7':'50.034',
        '8':'50.034', '9':'null', '10':'null', '11':'null',
        '12':'null', '13':'null', '14':'50.003', '15':'50.003',
        '16':'50.003', '17':'null', '18':'null'}, 
'wed': {'0':'null', '1':'50.005', '2':'50.005', '3':'50.005', 
        '4':'null', '5':'null', '6':'null', '7':'null',
        '8':'null', '9':'null', '10':'null', '11':'null',
        '12':'null', '13':'null', '14':'null', '15':'null',
        '16':'null', '17':'null', '18':'null'}, 
'thu': {'0':'50.034', '1':'50.034', '2':'50.034', '3':'50.034', 
        '4':'50.005', '5':'50.005', '6':'50.005', '7':'50.005',
        '8':'null', '9':'null', '10':'null', '11':'null',
        '12':'null', '13':'hass', '14':'hass', '15':'hass',
        '16':'hass', '17':'hass', '18':'hass'}, 
'fri': {'0':'50.003', '1':'50.003', '2':'50.003', '3':'50.003', 
        '4':'null', '5':'null', '6':'null', '7':'null',
        '8':'50.005', '9':'50.005', '10':'50.003', '11':'null',
        '12':'null', '13':'null', '14':'null', '15':'null',
        '16':'null', '17':'null', '18':'null'}}]

@app.route("/", methods =['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == "user" and password=="password":
            return redirect("http://127.0.0.1:5000/course_lead")
        else:
            message = "Failed Login"
            return render_template('login.html', message=message)
    return render_template('login.html')

@app.route("/course_lead", methods=['GET', 'POST'])
def submit_class_info():
    if request.method == 'POST':
        pillar = request.form['pillar']
        course_no = request.form['course_no']
        course_load = request.form['course_load']
        final_exam_time = request.form['final_exam']
        # these values will be sent to a database
        message = "Submit successfully!"
        return render_template('submit_info.html', message=message)
    else:
        return render_template('submit_info.html')

@app.route("/student_calendar", method=['GET', 'POST'])
def get_calendar():
    if request.method == 'POST':
        term = request.form['term']
        if term == '5':
            json = json.dumps(term5coh1)
        elif term == '7':
        else:

if __name__ == '__main__':
    app.run(debug=True)