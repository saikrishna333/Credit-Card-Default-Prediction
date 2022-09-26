# -*- coding: utf-8 -*-
"""app .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cVOt27IJGKwzZxQLGXHBPlkr92pHN4He
"""

# FLASK - deployment

import numpy as np
from werkzeug.wrappers import Request,Response
from flask import Flask,request,jsonify,render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('pipe.pkl', 'rb'))
# Default route set as 'home'
@app.route('/')

def home():
    return render_template('home.html') # Render home.html

# Route 'classify' accepts GET request
@app.route('/classify/',methods=['GET','POST'],endpoint='/classify')
def classify():
    try:
        lb = request.args.get('lb') # Get parameters for sepal length
        sex = request.args.get('sex') # Get parameters for sepal width
        edu = request.args.get('edu') # Get parameters for petal length
        mar = request.args.get('mar') # Get parameters for petal width
        age = request.args.get('age')
        p0 = request.args.get('p0')
        p2 = request.args.get('p2')
        p3 = request.args.get('p3')
        p4 = request.args.get('p4')
        p5 = request.args.get('p5')
        p6 = request.args.get('p6')
        b1 = request.args.get('b1')
        b2 = request.args.get('b2')
        b3 = request.args.get('b3')
        b4 = request.args.get('b4')
        b5 = request.args.get('b5')
        b6 = request.args.get('b6')
        pa1 = request.args.get('pa1')
        pa2 = request.args.get('pa2')
        pa3 = request.args.get('pa3')
        pa4 = request.args.get('pa4')
        pa5 = request.args.get('pa5')
        pa6 = request.args.get('pa6')
        
        # Get the output from the classification model
        #variety = model.classify(sepal_len, sepal_wid, petal_len, petal_wid)
        arr=np.array([lb,sex,edu,mar,age,p0,p2,p3,p4,p5,p6,b1,b2,b3,b4,b5,b6,pa1,pa2,pa3,pa4,pa5,pa6])
        query=arr.reshape(1,-1)
        output_mappings={0:'NO',1:"YES"}
        output=output_mappings[model.predict(query)[0]]
        # Render the output in new HTML page
        return render_template('output.html', output=output)
    except:
        return 'Error'

if(__name__=='__main__'):
    app.run(debug=False)



