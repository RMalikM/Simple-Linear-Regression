from joblib import Parallel, delayed
import joblib
  

def save_model(model, filename):

    # Save the model as a pickle in a file
    joblib.dump(model, filename+'.pkl')


def load_model(model_path):

    # Load the model from the file
    model = joblib.load(model_path)
    return model 