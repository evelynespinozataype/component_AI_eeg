import pickle

def cleaning_data(df_data):
    df_data = df_data.drop(columns=['attention', 'meditation'], axis=1)
    df_data.columns = ['delta','theta','low-alpha', 'high-alpha', 'low-beta', 'high-beta', 'low-gamma', 'mid-gamma']
    mapping = {df_data.columns[0]:'Delta', df_data.columns[1]: 'Theta', df_data.columns[2]:'Alpha1', df_data.columns[3]: 'Alpha2',df_data.columns[4]:'Beta1', df_data.columns[5]: 'Beta2',df_data.columns[6]:'Gamma1', df_data.columns[7]: 'Gamma2'}
    df_data = df_data.rename(columns=mapping)
    
def get_prediction(df):
    data = cleaning_data(df)
    filename = 'EEG_SVC_model.pickle'
    loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
    prediction=loaded_model.predict(data)
    print('prediction is ', prediction)
    return prediction