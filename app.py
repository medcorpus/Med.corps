from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/main_info')
def main_info():
    return render_template('main_info.html')

@app.route('/upgrade_system')
def upgrade_system():
    return render_template('upgrade_system.html')

@app.route('/awards')
def awards():
    return render_template('awards.html')

@app.route('/documentation')
def documentation():
    return render_template('documentation.html')

@app.route('/military_doctors')
def military_doctors():
    return render_template('military_doctors.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)