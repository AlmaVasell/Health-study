import numpy as np

class HealthAnalyzer:
    '''
    En klass som skapar statistiska analyser på
    datan från hälsostudien.
    '''
  
    def __init__(self, df):
        '''
        Initierar klassen med ett DataFrame
        '''
        self.df = df
        

    def mean_bp(self):
        '''
        Beräknar medelvärdet av blodtryck.
        '''
        return self.df["systolic_bp"].mean()

    def regression_age_weight(self):
        """
        Skapar en linjär regression som förutsäger systoliskt blodtryck
        baserat på ålder och vikt.
        """
        
        X_raw = self.df[["age", "weight"]].values
        y = self.df["systolic_bp"].values.reshape(-1, 1)

        ones = np.ones((X_raw.shape[0], 1))
        X = np.hstack([ones, X_raw])

        beta = np.linalg.inv(X.T @ X) @ (X.T @ y)

        y_pred = X @ beta

        return {
            "beta": beta.flatten(),
            "y_pred": y_pred.flatten(),
            "X": X,
            "y": y.flatten()
        }
