from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/')
def home():
    results_path = os.path.join(os.path.dirname(__file__), 'results.json')

    with open(results_path, 'r') as f:
        results = json.load(f)
    
    return render_template('index.html', results=results)


if __name__ == "__main__":
    app.run(debug=True)
