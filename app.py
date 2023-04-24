from flask import Flask, render_template

app: Flask = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/tracker')
def habit_tracker():
    return render_template('habit_tracker.html')

if __name__ == "__main__":
    app.run(debug=True)
