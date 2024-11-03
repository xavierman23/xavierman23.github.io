import pickle
from sklearn.neural_network import MLPRegressor
import pandas as pd
import warnings
warnings.filterwarnings("ignore")


def calculate(num1, op, num2):
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    
    exp = pd.DataFrame({"Num1": [num1], "Num2": [num2], "sub": [1 if op == "-" else 0], "mult": [1 if op == "*" else 0], "div": [1 if op == "/" else 0]})

    result = model.predict(exp)
    return result[0]


