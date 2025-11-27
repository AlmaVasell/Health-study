import pandas as pd
import numpy as np

def summary_statistics(df, columns):
    ''' Denna funktion beräknar medelvärde, median,
     min och max för valda kolumner.
     Returnerar ett dictionary med resultat för varje kolumn
     '''
    result = {}
    for col in columns:
        series = df[col]
        result[col] = {
            "mean": float(series.mean()),
            "median": float(series.median()),
            "min": float(series.min()),
            "max": float(series.max())
        }
    return result
