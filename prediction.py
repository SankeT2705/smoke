import pickle

file = "Final.pkl"
load = pickle.load(open(file, 'rb'))


def predict(arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9, arg10, arg11, arg12, arg13):
    pred = load.predict([[arg1, arg2, arg3, arg4, arg5, arg6,
                        arg7, arg8, arg9, arg10, arg11, arg12, arg13]])
    if pred[0] == 1:
        return "High Fire Chance"
    else:
        return "Low Fire Chance"
