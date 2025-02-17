from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Photos Page
@app.route('/photos')
def photos():
    return render_template('photos.html')

# RSVP Page
@app.route('/rsvp')  
def rsvp():
    return render_template('rsvp.html')

# RSVP Form Submission
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    attending = request.form.get('attending')
    return render_template('result.html', name=name, attending=attending)

# Serve favicon.ico to prevent 404 errors
@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True)
