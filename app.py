from flask import Flask, render_template, request, json

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/signUp')
def signUp():
    return render_template('NeocaseCaseForm.html')

from sklearn.externals import joblib
classifier = joblib.load('SGDClassifier Model/model.pkl')

@app.route('/predictions', methods=['POST'])
def predictions():
    text =  request.form['text'];
    category = classifier.predict([text])[0]
    return category;

if __name__=="__main__":
    app.run()
