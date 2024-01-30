def load_template(template_name):
    templates = {
        'index': """
            <!-- Ursina-like HTML code for the index screen -->
            <h1>Welcome to the Quiz App!</h1>
            <a href="{{ url_for('create_quiz') }}">Create Quiz</a>
            <a href="{{ url_for('take_quiz') }}">Take Quiz</a>
            <a href="{{ url_for('quiz_library') }}">Quiz Library</a>
        """,
        'create_quiz': """
            <!-- Ursina-like HTML code for the create quiz screen -->
            <h1>Create Your Quiz Here</h1>
            <form action="{{ url_for('create_quiz') }}" method="post">
                <!-- Add your create quiz form content here -->
                <button type="submit">Submit Quiz</button>
            </form>
            <a href="{{ url_for('home') }}">Back</a>
        """,
        'take_quiz': """
            <!-- Ursina-like HTML code for the take quiz screen -->
            <h1>Take a Quiz</h1>
            <!-- Add your take quiz content here -->
            <a href="{{ url_for('home') }}">Back</a>
        """,
        'quiz_library': """
            <!-- Ursina-like HTML code for the quiz library screen -->
            <h1>Quiz Library</h1>
            <!-- Add your quiz library content here -->
            <a href="{{ url_for('home') }}">Back</a>
        """
    }
    
    return templates.get(template_name, '')
