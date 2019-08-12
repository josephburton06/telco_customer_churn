import warnings
warnings.filterwarnings("ignore")

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

import jb_helper_functions_prep
from jb_helper_functions_prep import create_enc

def prep_telco_df():
    df = pd.read_csv('telco_churn.csv')
    df.columns = [x.lower() for x in df.columns]
    df = df[df.tenure > 0]
    df['totalcharges'] = df['totalcharges'].astype(str).astype(float)
    df = create_enc(df, ['gender', 'partner', 'dependents', 'phoneservice', 'multiplelines', 'internetservice',
       'onlinesecurity', 'onlinebackup', 'deviceprotection', 'techsupport',
       'streamingtv', 'streamingmovies', 'contract', 'paperlessbilling',
       'paymentmethod', 'churn'])
    
    return df