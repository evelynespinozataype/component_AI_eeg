#connection from AI_EEG to Aquarela
import socketio

# Create a SocketIO client instance
sio = socketio.Client()

@sio.on('connect')
def on_connect():
    print('Connected to server')

@sio.on('disconnect')
def on_disconnect():
    print('Disconnected from server')

# Establishing a SocketIO connection to Aquarela server
sio.connect('http://localhost:3000')

# Emit the "heart_rate" event with a heart rate value
heart_rate_flag = 1  # Feliz
sio.emit('component_heart_rate', heart_rate_flag)

brain_wave_flag = 1  # happy=1, sad=0
sio.emit('component_brain_wave', brain_wave_flag)

# Function ECG to send the Flag of emotional state in HeartRate
def sendValueToAquarela(brain_wave_flag):
    brain_wave_flag = 1  # happy=1, sad=0
    sio.emit('component_brain_wave', brain_wave_flag)


# Wait for a moment to allow the event to be sent
sio.sleep(2)

# Disconnect from the server
sio.disconnect()
