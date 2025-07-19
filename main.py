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
