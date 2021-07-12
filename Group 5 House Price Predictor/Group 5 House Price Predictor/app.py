import numpy as np
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''

    features = [(x) for x in request.form.values()] # Fetching user input values

    statezip_encoded = [62, 58, 26, 7, 31, 54, 23, 27, 67, 48, 42, 49, 6, 45, 73,  5, 46, 9, 60, 2, 63, 21, 17, 56, 22, 41, 13, 50, 68, 55, 14, 33, 44, 15, 37, 43, 10, 38, 74, 32, 36, 59, 47, 53, 4, 57, 70, 3, 11, 64, 69, 0, 34, 65, 16, 66, 35, 25, 8, 30, 19, 52, 18, 61, 20, 71, 75, 51, 40, 72, 1, 24, 12, 39, 28, 29, 76]

    statezip = ['WA 98133','WA 98119','WA 98042','WA 98008','WA 98052','WA 98115','WA 98038','WA 98045','WA 98155','WA 98105','WA 98074','WA 98106','WA 98007','WA 98092','WA 98198','WA 98006','WA 98102','WA 98011','WA 98125','WA 98003','WA 98136','WA 98033','WA 98029','WA 98117','WA 98034','WA 98072','WA 98023','WA 98107','WA 98166','WA 98116','WA 98024','WA 98055','WA 98077','WA 98027','WA 98059','WA 98075','WA 98014','WA 98065','WA 98199','WA 98053','WA 98058','WA 98122','WA 98103','WA 98112','WA 98005','WA 98118','WA 98177','WA 98004', 'WA 98019','WA 98144','WA 98168','WA 98001','WA 98056','WA 98146','WA 98028','WA 98148','WA 98057','WA 98040','WA 98010','WA 98051','WA 98031','WA 98109','WA 98030','WA 98126','WA 98032','WA 98178','WA 98288','WA 98108','WA 98070','WA 98188','WA 98002','WA 98039','WA 98022','WA 98068','WA 98047','WA 98050','WA 98354']


    x=features[-1]
    for i in range(0,77):
        if statezip[i]==x:
            a=statezip_encoded[i]

    z = np.zeros(77)
    z[a] = 1
    features.pop(-1)
    features = np.array([float(x) for x in  features])
    b = np.concatenate((features,z), axis=0)


    # Encoding Statezip value



    final_features = np.array([b])
    final_features.reshape((-1,1))
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    return render_template('index.html', prediction_text='House price should be $ {}'.format(output))
    # return render_template('index.html', prediction_text='House price should be $ {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)
