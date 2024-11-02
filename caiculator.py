from sklearn.neural_network import MLPRegressor
import pandas as pd
import numpy

def main():
    training = pd.read_csv("caiculator_data.csv")

    X = (changeSign(training)).to_numpy()
    y = numpy.transpose(training[["Equals"]].to_numpy())[0]

    print(y)

    model = MLPRegressor(random_state=0, max_iter=500).fit(X, y)

    testDF = pd.DataFrame({"Num1": [7, 2.8, 5, 2, 3, 8.2, 100],
            "Num2": [4, 4.5, 2, 1, 3, 7, 266],
            "Sign": ["+", "-", "*", "+", "*", "-", "+"]})
    

    test = changeSign(testDF).to_numpy()


    testOut = list(model.predict(test))

    testDF["result"] = testOut
    print(testDF)


def changeSign(df):
    result = pd.DataFrame()
    result["Num1"] = df["Num1"]
    result["Num2"] = df["Num2"]
    result["add"] = (df["Sign"] == "+").astype(int)
    result["sub"] = (df["Sign"] == "-").astype(int)
    result["mult"] = (df["Sign"] == "*").astype(int)
    result["div"] = (df["Sign"] == "/").astype(int)
    return result

if __name__ == "__main__":
    main()