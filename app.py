import csv
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'sacke_e_fin'

@app.before_request
def before_request():
    session.setdefault('current_quiz', [])
    session.setdefault('quiz_library', [])

def save_to_csv(quiz_name, questions):
    with open('quiz_library.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([quiz_name, questions])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create_quiz', methods=['GET', 'POST'])
def create_quiz():
    if request.method == 'POST':
        session['creating_quiz'] = False
        return redirect(url_for('home'))

    session['creating_quiz'] = True
    return render_template('create_quiz.html')

@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    if request.method == 'POST':
        if session.get('creating_quiz', False):
            session['current_quiz'] = []

            for i in range(6):
                question = request.form.get(f'question_{i}')
                option_a = request.form.get(f'option_A_{i}')
                option_b = request.form.get(f'option_B_{i}')
                option_c = request.form.get(f'option_C_{i}')
                option_d = request.form.get(f'option_D_{i}')
                correct_answers = request.form.getlist(f'correct_answers_{i}')

                current_question = {
                    'question': question,
                    'options': [option_a, option_b, option_c, option_d],
                    'correct_answers': correct_answers
                }

                session['current_quiz'].append(current_question)

        return render_template('create_quiz.html')

@app.route('/finish_quiz', methods=['POST'])
def finish_quiz():
    if 'current_quiz' in session:
        session['creating_quiz'] = False
        return render_template('create_quiz.html')
    return redirect(url_for('home'))

@app.route('/add_to_library', methods=['POST'])
def add_to_library():
    if 'current_quiz' in session:
        quiz_name = request.form.get('quiz_name')
        if session['current_quiz']:
            save_to_csv(quiz_name, session['current_quiz'])
            session.pop('current_quiz', None)
            session['creating_quiz'] = False

            if 'quiz_library' not in session:
                session['quiz_library'] = []

            session['quiz_library'].append({
                'name': quiz_name,
                'questions': session['current_quiz']
            })

    return redirect(url_for('create_quiz'))

@app.route('/quiz_library')
def quiz_library():
    return render_template('quiz_library.html')

@app.route('/take_quiz/<quiz_name>', methods=['GET', 'POST'])
def take_quiz(quiz_name):
    return render_template('take_quiz.html', quiz_name=quiz_name)

if __name__ == '__main__':
    app.run(debug=True)
