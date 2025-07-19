from flask import Flask, render_template, send_from_directory, abort, jsonify
import os

# 👉 নিশ্চিতভাবে static ও template ফোল্ডার নির্দিষ্ট করা হচ্ছে
app = Flask(__name__, static_folder='static', template_folder='templates')


@app.route('/')
def home():
    return render_template("dashboard.html")   # ✅ templates/dashboard.html থেকে লোড হবে


@app.route('/game')
def game():
    return render_template("index.html")       # ✅ templates/index.html থেকে লোড হবে


# 🔎 Debugging রাউট - লাইভ ফাইল লিস্ট দেখতে
@app.route('/debug')
def debug():
    files = os.listdir('.')
    html_files = []
    for root, dirs, filenames in os.walk('.'):
        for f in filenames:
            if f.endswith('.html'):
                html_files.append(os.path.join(root, f))
    return jsonify({
        'all_files': files,
        'html_files': html_files,
        'current_directory': os.getcwd()
    })


# ⚠️ Static fallback route (rarely needed but added for safety)
@app.route('/<path:filename>')
def static_files(filename):
    try:
        return send_from_directory('.', filename)
    except FileNotFoundError:
        abort(404)


# ✅ Disable caching (helpful for Render CDN)
@app.after_request
def after_request(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
