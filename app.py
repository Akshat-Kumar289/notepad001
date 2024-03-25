import subprocess
from flask import Flask, render_template, request

app = Flask(__name__)

# Function to commit changes using Git
def commit_changes(message):
    try:
        subprocess.run(['git', 'add', '.'])
        subprocess.run(['git', 'commit', '-m', message])
        return True
    except Exception as e:
        print("Error committing changes:", e)
        return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save():
    content = request.form['content']
    if commit_changes("Changes committed via the web interface"):
        return "Changes committed successfully!"
    else:
        return "Failed to commit changes."

if __name__ == '__main__':
    app.run(debug=True)
    