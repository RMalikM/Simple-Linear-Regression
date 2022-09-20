import numpy as np


# Simple Linear Regression
class Simple_LR:
    
    def __init__(self):
        self.slope = 0
        self.intercept = 0
        
    def fit(self, X_train, y_train):
        nr = 0
        dr = 0
        
        for i in range(len(X_train)):
            nr = nr + ((X_train[i] - X_train.mean()) * (y_train[i] - y_train.mean()))
            dr = dr + ((X_train[i] - X_train.mean()) * (X_train[i] - X_train.mean()))
        
        # slope or regression coefficient
        self.slope = nr / dr
        
        # intercept
        self.intercept = y_train.mean() - (self.slope * X_train.mean())
        
        print('Regression coefficient: ', self.slope)
        print('Intercept: ', self.intercept)
        
    def predict(self, X_test):            
        return (self.intercept + (self.slope * X_test)).reshape(len(X_test,))            