"""
Modulo helpers para el preprox de datos

"""

import numpy as np

def get_numerical_features(df):
    return df.select_dtypes(include=[np.number]).columns