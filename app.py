from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/imgEdit')
def imgEditor():
    return render_template('image.html')

@app.route('/pdfEdit')
def pdfEditor():
    return render_template('pdf.html')

@app.route('/videoEdit')
def videoEditor():
    return render_template('video.html')

@app.route('/fileEdit')
def fileEditor():
    return render_template('file.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)