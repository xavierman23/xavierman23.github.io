from sklearn.neural_network import MLPRegressor
import pandas as pd
import numpy
from sklearn.model_selection import train_test_split


def main():
    training = pd.read_csv("caiculator_data.csv")

    X = (changeSign(training)).to_numpy()
    y = numpy.transpose(training[["Equals"]].to_numpy())[0]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = MLPRegressor(hidden_layer_sizes= (100, 100, 100, 100, 100, 100, 100, 100, 100, 100), 
                         random_state=0, max_iter=500, learning_rate = "adaptive").fit(X_train, y_train)

    testDF = pd.DataFrame({"Num1": [7, 2.8, 5, 2, 3, 8.2, 100],
            "Num2": [4, 4.5, 2, 1, 3, 7, 266],
            "Sign": ["+", "-", "*", "+", "*", "-", "+"]})
    

    test = changeSign(X_test).to_numpy()


    testOut = list(model.predict(test))

    testDF["result"] = testOut
    print(testDF)


def changeSign(df):
    result = pd.DataFrame()
    result["Num1"] = df["Num1"]
    result["Num2"] = df["Num2"]
    result["sub"] = (df["Sign"] == "-").astype(int)
    result["mult"] = (df["Sign"] == "*").astype(int)
    result["div"] = (df["Sign"] == "/").astype(int)
    return result

if __name__ == "__main__":
    main()