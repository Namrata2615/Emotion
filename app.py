from flask import Flask,render_template,request,jsonify
import pandas as pd
import numpy as np 
import joblib

app = Flask(__name__)

model = joblib.load('emotion_model.pkl')

@app.route('/',methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    message = request.form.get('message')
    output = model.predict([message])
    if output == ["sadness"]:
      result = "sadness"
    elif output ==["anger"]:
      result = "anger" 
    elif output ==["love"]:
      result = "love" 
    elif output ==["surprise"]:
      result = "surprise" 
    elif output ==["fear"]:
     result = "fear" 
    else:
      result = "happy" 
    return render_template('index.html', result=result,message=message)      

  else:
    return render_template('index.html')  


if __name__ == '__main__':
    app.run(debug=True)