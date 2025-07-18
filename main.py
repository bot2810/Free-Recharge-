
from flask import Flask, render_template, send_from_directory, abort
import os

app = Flask(__name__, static_folder='.', template_folder='.')

@app.route('/')
def dashboard():
    try:
        return send_from_directory('.', 'dashboard.html')
    except FileNotFoundError:
        abort(404)

@app.route('/game')
def game():
    try:
        return send_from_directory('.', 'index.html')
    except FileNotFoundError:
        abort(404)

@app.route('/<path:filename>')
def static_files(filename):
    try:
        return send_from_directory('.', filename)
    except FileNotFoundError:
        abort(404)

@app.after_request
def after_request(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
