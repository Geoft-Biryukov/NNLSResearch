import numpy as np

def CreateLeastSquareProblemBro():
    a = np.array([[73, 71, 52], [87, 74, 46], [72, 2, 7], [80, 89, 871]])
    b = np.array([49, 67, 68, 20])
    res = np.array([0.649538436402255, 0, 0])
    return (a, b, res)

def CreateLeastSquareProblemHansen():
    a = np.array([[0.16, 0.10], [0.17, 0.11], [2.02, 1.21]])
    b = np.array([0.27, 0.25, 3.33])
    res = np.array([1.647512636339452, 0])
    return (a, b, res)