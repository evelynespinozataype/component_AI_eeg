import pickle

def get_prediction():
    eeg_heart_rate = float(request.form['heart_rate'])
    loaded_model = pickle.load(open(filename, 'rb'))
    prediction=loaded_model.predict(X_happ1)
    print(prediction)
    