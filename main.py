from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send
import numpy as np
import pandas as pd
import scipy as sp
import scipy.fftpack
from scipy.signal import find_peaks
from datetime import datetime
from remote import *
from ai_eeg import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

def saving_file(df):
    now = datetime.now()
    path_name = 'data/raw_eeg_'+ now.strftime('%Y-%m-%d_%H-%M') +'.csv'
    df.to_csv(path_name, mode='a', index=False, header=False)

def recognition_emotionalstate(data):
    cod_emotion = ''
    df = pd.DataFrame(eval(data))
    saving_file(df)
    emotion_ft = recognition_ft(df)
    emotion_svm = recognition_svm(df)
    print('FT: ',emotion_ft)
    print('SVM: ',emotion_svm)
    if emotion_ft == '82' or emotion_svm == '82':
        cod_emotion = '82'
    if emotion_ft == '84' or emotion_svm == '84':
        cod_emotion = '84'
    return cod_emotion

def recognition_svm(df):
    emotion = get_prediction(df)

def recognition_ft(df):
    countpeaks, peak2peak = fouriertransform(df)
    cod_emotion = calculate_emotion(countpeaks, peak2peak)
    return cod_emotion

def calculate_emotion(countpeaks, peak2peak):
    # Happy countpeaks < 20 and peak2peak >= 0.98
    # Sad countpeaks > 20 and peak2peak <= 0.98
    cod_emotion = ''
    if ((countpeaks < 20) and (peak2peak >= 0.98)):
        cod_emotion = '82'
    if ((countpeaks > 20) and (peak2peak <= 0.98)):
        cod_emotion = '84'
    return cod_emotion

def fouriertransform(df):
    df_gamma = df.iloc[:, 10] # [:, 10] columna Gamma 1 (Low gamma)
    F_gamma = np.fft.fft(df_gamma) #Fourier
    F_gamma = np.abs(F_gamma) #Normalizing
    F_gamma = F_gamma/F_gamma.max() #Normalizing
    peaks = find_peaks(F_gamma, height = 0, threshold = 0, distance = 1)
    numpeaks = peaks[0] #list of the heights of the peaks
    countpeaks = len(numpeaks) #count peaks
    peak2peak = np.ptp(F_gamma, axis=0) #distance max peak2peak
    print("count Peaks:",countpeaks, " Peak2peak:", round(peak2peak,2)) #Periodo
    return countpeaks, peak2peak

def send_aquarela():
     return 1

@socketio.on('join_comp_brainwave_app', namespace='/remote_eegapp')
def handle_brainwave(data):
    socketio.emit('sending_brainwaves', data)#send to web
    cod_emotion = recognition_emotionalstate(data)
    print("---emotional state: ",cod_emotion)
    #sendValueToAquarela(cod_emotion)#send to Aquarela

if __name__=='__main__':
	socketio.run(app, host='0.0.0.0', port=4000, debug=True)
