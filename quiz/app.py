from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create_quiz')
def create_quiz():
    return render_template('create_quiz.html')

@app.route('/take_quiz')
def take_quiz():
    return render_template('take_quiz.html')

@app.route('/quiz_library')
def quiz_library():
    return render_template('quiz_library.html')

if __name__ == '__main__':
    app.run(debug=True)
