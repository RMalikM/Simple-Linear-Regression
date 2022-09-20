import numpy as np


''' Simple Linear Regression (SLR) Metrices: 
        * Mean absolute error (mae)
        * Mean squared error (mse)
        * R-squared (r2)
    '''
class slr_metrices:
    
    def __init__(self):
        self.mae = float('inf')
        self.mse = float('inf')
        self.r2 = 0
        
    def MAE(self, y_true, y_pred):
        self.mae = np.mean(np.abs(y_true - y_pred))
        return self.mae
    
    def MSE(self, y_true, y_pred):
        self.mse =  np.mean((y_true - y_pred)**2)
        return self.mse
        
    def R_squared(self, y_true, y_pred):
        y_true_mean = np.mean(y_true)
        
        ssr = np.sum((y_true - y_pred)**2)
        ssm = np.sum((y_true - y_true_mean)**2)
        self.r2 = 1 - (ssr/ssm)
        return self.r2