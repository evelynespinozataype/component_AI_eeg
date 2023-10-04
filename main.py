from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send
import numpy as np
import pandas as pd
import scipy as sp
import scipy.fftpack
from scipy.signal import find_peaks

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

def identify_emotionalstate(data):
    df = pd.DataFrame(eval(data))  #eval to pass from string to a data type of 
    df.to_csv('raw.csv', mode='a', index=False, header=False)
    countpeaks, peak2peak = fouriertransform(df)
    status = calculate_emotion(countpeaks, peak2peak)
    return status

def calculate_emotion(countpeaks, peak2peak):
    # Happy countpeaks < 20 and peak2peak >= 0.98
    # Sad countpeaks > 20 and peak2peak <= 0.98
    status = 'none'
    if ((countpeaks < 20) and (peak2peak >= 0.98)):
        status = 'happy'
    else:
        status = 'none'
    if ((countpeaks > 20) and (peak2peak <= 0.98)):
        status = 'sad'
    else:
        status = 'none'
    return status

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
    
@socketio.on('join_comp_brainwave_app', namespace='/remote')
def handle_brainwave(data):
	#print("--Receiving: BrainWave data: ",data)
	socketio.emit('sending_brainwaves', data)
	status = identify_emotionalstate(data)
	print("---emotional state: ",status)

if __name__=='__main__':
	socketio.run(app, host='0.0.0.0', port=4000, debug=True)
      
#@socketio.on('mensaje')
#def handle_message(data):
#    print('mensaje: ' + data)

#@socketio.on('brain_data')
#def coracao(data):
#	print("BrainWave data: ",data)
#	emit('messageserver',data)

#@socketio.on('message')
#def handleBrainWave(data):
#    print("Brain Waves:",data)
#    socketio.emit('messageserver',data)
#socketio.emit('messageserver',[1,2,3,4,5,6])
