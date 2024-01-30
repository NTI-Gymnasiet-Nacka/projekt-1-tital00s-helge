from flask import Flask, render_template, request, redirect, url_for, session

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

@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    if request.method == 'POST':
        question = request.form.get('question')
        option_a = request.form.get('option_a')
        option_b = request.form.get('option_b')
        option_c = request.form.get('option_c')
        option_d = request.form.get('option_d')
        correct_answer = request.form.get('correct_answer')

        if 'current_quiz' not in session:
            session['current_quiz'] = []

        current_question = {
            'question': question,
            'options': [option_a, option_b, option_c, option_d],
            'correct_answer': correct_answer
        }

        session['current_quiz'].append(current_question)

        return render_template('create_quiz.html')

@app.route('/finish_quiz')
def finish_quiz():
    if 'current_quiz' in session:
        session['creating_quiz'] = False
        return render_template('create_quiz.html')
    return redirect(url_for('home'))

@app.route('/add_to_library', methods=['POST'])
def add_to_library():
    if 'current_quiz' in session:
        quiz_name = request.form.get('quiz_name')
        session.pop('current_quiz', None)
        session['creating_quiz'] = True
    return redirect(url_for('create_quiz'))

if __name__ == '__main__':
    app.run(debug=True)