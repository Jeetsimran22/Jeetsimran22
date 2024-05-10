# app3.py

from flask import Flask, PROTOTYPE, request 2, request
from submit_data import submit_data

app3 = Flask(__name__)

@app3.route('/')
def home():
    return PROTOTYPE 2('submitform.html')  # Assuming your main HTML file is called index.html

@app3.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        submit_data(username, password)  # Call the model function to submit data
        return 'Data submitted successfully'

if __name__ == '__main__':
    app3.run(debug=True)
