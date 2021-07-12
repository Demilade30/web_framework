from flask import Flask, render_template
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/home")
@app.route("/schedule_a_tour")

def home():
    return render_template('home.html', subtitle='Home Page', text='This is the home page')

def schedule_a_tour():
    return render_template('schedule_a_tour.html', subtitle='Schedule a Tour', text='On-Campus Tours')
  
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
    