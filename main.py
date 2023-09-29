from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send
import pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

#@app.route('/main',methods= ['POST','GET'])
#def quadro_desenho():
#    return render_template('index.html')

def create_dataframe(data):
    df = pd.DataFrame(eval(data))#eval to pass from string to a data type of 
    df.to_csv('raw.csv', mode='a', index=False, header=False)
    return df

@socketio.on('mensaje')
def handle_message(data):
    print('message: ' + data)

#@socketio.on('connect', namespace='/main')
#def client_connect():
#    socketio.emit('event', { 'type': 'client_connect' }, namespace='/main')
    
@socketio.on('join_comp_brainwave_app')
def handle_brainwave(data):
	print("BrainWave data: ",data)
	socketio.emit('sending_brainwaves', data)
    #emit('messageserver',data,json=True,namespace='/index')
	#df = create_dataframe(data)
	#print("DATAFRAME: ",df)

#@socketio.on('brain_data')
#def coracao(data):
#	print("BrainWave data: ",data)
#	emit('messageserver',data)

#@socketio.on('message')
#def handleBrainWave(data):
#    print("Brain Waves:",data)
#    socketio.emit('messageserver',data)
#socketio.emit('messageserver',[1,2,3,4,5,6])

if __name__=='__main__':
 	#socket_io.run(app, host='0.0.0.0', port=80, debug=True)
	socketio.run(app, host='0.0.0.0', port=4000, debug=True)