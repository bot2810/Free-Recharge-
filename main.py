from flask import Flask, render_template, send_from_directory, abort, jsonify
import os

# ✅ এখন সঠিকভাবে static ও template ফোল্ডার বলছি
app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/')
def home():
    return render_template("dashboard.html")   # ❗ এখন template ফোল্ডার থেকে লোড হবে


@app.route('/game')
def game():
    return render_template("index.html")       # ❗ index.html লোড করবে templates থেকে


# ✅ স্ট্যাটিক ফাইল সার্ভ করার রুট (অপ্রয়োজনীয় হলে বাদ দিতে পারো)
@app.route('/<path:filename>')
def static_files(filename):
    try:
        return send_from_directory('.', filename)
    except FileNotFoundError:
        abort(404)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

from flask import Flask, render_template, send_from_directory, abort, jsonify
import os

app = Flask(__name__, static_folder='.', template_folder='.')

@app.route('/debug')
def debug():
    files = os.listdir('.')
    html_files = [f for f in files if f.endswith('.html')]
    return jsonify({
        'all_files': files,
        'html_files': html_files,
        'current_directory': os.getcwd()
    })

@app.route('/')
def dashboard():
    if not os.path.exists('dashboard.html'):
        return f"dashboard.html ফাইল পাওয়া যায়নি। Available files: {os.listdir('.')}", 404
    return send_from_directory('.', 'dashboard.html')

@app.route('/game')
def game():
    if not os.path.exists('index.html'):
        return f"index.html ফাইল পাওয়া যায়নি। Available files: {os.listdir('.')}", 404
    return send_from_directory('.', 'index.html')

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
    
