import socketio
sio = socketio.Client()# Create a SocketIO client instance

@sio.on('connect')
def on_connect():
    print('Connected to server')

@sio.on('disconnect')
def on_disconnect():
    print('Disconnected from server')

# Establishing a SocketIO connection to Aquarela server
sio.connect('http://192.168.15.5:3000', namespaces=['/remoteg'])

# Emiting the heartrate to component_aquarela
heart_rate_flag = 1  # Feliz
sio.emit('join_component_heartrate', heart_rate_flag, namespace='/remoteg')

# Emiting the brainwave to component_aquarela
brain_wave_flag = 1  # happy=1, sad=0
sio.emit('join_component_brainwave', brain_wave_flag, namespace='/remoteg')

# Function ECG to send the Flag of emotional state in HeartRate
def sendValueToAquarela(status):
    print("Enviando datos para Aquarela")
    brain_wave_flag = 1  # happy=1, sad=0
    sio.emit('join_component_brainwave', brain_wave_flag,  namespace='/remoteg')

# Receving from the component_brainwave_app
#@sio.on('join_component_brainwave_app')
#def component_brainwave_app(data):
#	print("BrainWave data: ",data)
     
# Wait for a moment to allow the event to be sent
#sio.sleep(2)

# Disconnect from the server
#sio.disconnect()
