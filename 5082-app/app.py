from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Initialize lists to store numbers
completed_numbers = []
excluded_numbers = []

def generate_random_number():
    """Generates a random number between 1 and 25, 
    excluding numbers in the excluded_numbers list and avoiding duplicates."""
    
    available_numbers = set(range(1, 26)) - set(excluded_numbers) - set(completed_numbers)
    if available_numbers:
        new_number = random.choice(list(available_numbers))
        completed_numbers.append(new_number)
        return new_number
    else:
        return None

@app.route('/')
def index():
    """Renders the HTML template with initial values."""
    
    all_done = False  # Initially, presentations are not completed
    return render_template('index.html', 
                           number=None,  # No number is displayed initially
                           completed=completed_numbers, 
                           excluded=excluded_numbers,
                           all_done=all_done)

@app.route('/generate_number')
def generate_number():
    """Generates a new number and returns it along with the all_done flag."""
    new_number = generate_random_number()
    all_done = len(completed_numbers) == 25
    return jsonify({'number': new_number, 'all_done': all_done})

@app.route('/get_completed_numbers')
def get_completed_numbers():
    """Returns the completed_numbers list as JSON."""
    return jsonify(completed_numbers)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)