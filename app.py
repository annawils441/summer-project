from flask import Flask, render_template

# Create Flask application instance
app = Flask(__name__, template_folder='templates')

# Create a route (URL endpoint)
# Create Homepage route
@app.route('/')
def homepage():
    return render_template('index.html')

# Create a Login route
@app.route('/login')
def login_page():
    return render_template('login.html')

# Create a Register route
@app.route('/register')
def register_page():
    return render_template('register.html')

# Create a Timetable route
@app.route('/timetable')
def timetable_page():
    return render_template('timetable.html')

@app.route('/timetable/coach')
def timetable_coach():
    return render_template('timetable-coach.html')

@app.route('/timetable/day')
def timetable_day():
    return render_template('timetable-day.html')

@app.route('/timetable/grade')
def timetable_grade():
    return render_template('timetable-grade.html')

@app.route('/secret')
def halloween_page():
    return render_template('halloween.html')

if __name__ == '__main__':
    app.run(debug=True)

