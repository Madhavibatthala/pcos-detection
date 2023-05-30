from flask import Flask, render_template, request

import pickle
import numpy as np

app = Flask(__name__)

# Load the trained machine learning model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define the home page
@app.route('/')
def index():
    return render_template('index.html')

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input values from the form
    age = float(request.form['age'])
    Weight = float(request.form['weight'])
    Height= float(request.form['height'])
    BMI = float(request.form['bmi'])
    BloodGroup=float(request.form['bg'])
    PulseRate=float(request.form['pr'])
    RR=float(request.form['rr'])
    hemoglogin=float(request.form['hb'])
    MenstrurationCycle=float(request.form['cycle'])
    CycleLength=float(request.form['length'])
    MarraigeStatus=float(request.form['ms'])
    Pragnancies=float(request.form['Pregnant'])
    NoOfObortions=float(request.form['oborptions'])
    Ibetahcg=float(request.form['Ihcg'])
    IIbetahcg=float(request.form['IIhcg'])
    FSH=float(request.form['fsh'])
    LH=float(request.form['lh'])
    FSHLH=float(request.form['fsh-lh'])
    HIP=float(request.form['hip'])
    weist=float(request.form['weist'])
    HIPWEIST=float(request.form['hip-weist'])
    TSH=float(request.form['tsh'])
    AMH=float(request.form['amh'])
    PRL=float(request.form['prl'])
    VitD3=float(request.form['d3'])
    PRG=float(request.form['prg'])
    RBS=float(request.form['rbs'])
    WeightGain=float(request.form['wg'])
    HairGrowth=float(request.form['hg'])
    Skindarkening=float(request.form['sk'])
    HairLoss=float(request.form['hl'])
    Pimples=float(request.form['pimples'])
    FastFood=float(request.form['fastfood'])
    RaguralExercise=float(request.form['re'])
    BP_Systolic=float(request.form['bps'])
    BP_diastolic=float(request.form['bpd'])
    # Follicle=float(request.form['fnr'])
    FollicleL=float(request.form['fnl'])
    FollicleR=float(request.form['fnr'])
    AVGFSIZEL=float(request.form['fsizel'])
    AVGFSIZER=float(request.form['fsizer'])
    Endomatrium=float(request.form['en'])



    # Convert the input values into a numpy array
    input_features = np.array([[age,Weight,Height,BMI,BloodGroup,PulseRate,RR,hemoglogin,MenstrurationCycle,CycleLength,MarraigeStatus,Pragnancies,NoOfObortions,
                                Ibetahcg,IIbetahcg,FSH,LH,FSHLH,HIP,weist,HIPWEIST,TSH,AMH,PRL,VitD3,PRG,RBS,WeightGain,HairGrowth,Skindarkening,HairLoss,Pimples,FastFood,RaguralExercise,BP_Systolic,BP_diastolic,FollicleL,FollicleR,AVGFSIZEL,AVGFSIZER,Endomatrium]])

    # Use the trained model to make a prediction
    prediction = model.predict(input_features)[0]

    # Determine the prediction text to display on the result page
    if prediction == 1:
        prediction_text = 'You are at risk of PCOS disease.'
        return render_template('result1.html', prediction_text=prediction_text)
    else:
        prediction_text = 'You are NOT at risk of PCOS disease.'
        return render_template('result2.html', prediction_text=prediction_text)

    # Render the result page with the prediction text
    

if __name__ == '__main__':
    app.run(debug=True)