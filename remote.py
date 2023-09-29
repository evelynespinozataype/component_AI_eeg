import socketio
sio = socketio.Client()# Create a SocketIO client instance

@sio.on('connect')
def on_connect():
    print('Connected to server')

@sio.on('disconnect')
def on_disconnect():
    print('Disconnected from server')

# Establishing a SocketIO connection to Aquarela server
sio.connect('http://localhost:3000')

# Emiting the heartrate to component_aquarela
heart_rate_flag = 1  # Feliz
sio.emit('component_heart_rate', heart_rate_flag)

# Emiting the brainwave to component_aquarela
brain_wave_flag = 1  # happy=1, sad=0
sio.emit('component_brain_wave', brain_wave_flag)

# Function ECG to send the Flag of emotional state in HeartRate
def sendValueToAquarela(brain_wave_flag):
    brain_wave_flag = 1  # happy=1, sad=0
    sio.emit('component_brain_wave', brain_wave_flag)

# Receving from the component_brainwave_app
#@sio.on('join_component_brainwave_app')
#def component_brainwave_app(data):
#	print("BrainWave data: ",data)
     
# Wait for a moment to allow the event to be sent
sio.sleep(2)

# Disconnect from the server
sio.disconnect()
