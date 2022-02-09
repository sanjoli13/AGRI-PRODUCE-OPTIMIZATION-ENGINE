#Importing the libraries
import pickle
from flask import Flask, render_template, request

#Global variables
app = Flask(__name__)
loadedModel = pickle.load(open('crop.pkl', 'rb'))

#User defined Functions
@app.route("/", methods=['GET'])
def Home():
    return render_template('shiv.html')

@app.route('/predictions', methods=['POST'])
def predict():
    N = request.form['N']
    P = int(request.form['P'])
    K = float(request.form['K'])
    temp = int(request.form['temp'])
    humidity = int(request.form['humidity'])
    ph = request.form['ph']
    rain = request.form['rain']
    predictions = loadedModel.predict([[N,P,K,temp,humidity,ph,rain]])[0]
    pred = 'Crop will be' + " " + predictions

    return render_template('shiv.html', Predict = pred)


#Main function
if __name__== "__main__":
    app.run(debug=True)