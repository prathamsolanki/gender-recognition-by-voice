import numpy as np
import pandas as pd
from scipy import sparse
import xgboost as xgb
from sklearn import model_selection, preprocessing, ensemble
from sklearn.metrics import log_loss
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.cross_validation import train_test_split

def runXGB(X, y):
    param = {}
    param['objective'] = 'binary:logistic'
    param['eta'] = 0.01                     #default: 0.3
    param['max_depth'] = 6                  #default: 6
    param['silent'] = 1
    param['gamma'] = 0                      #default: 0
    param['eval_metric'] = "logloss"
    param['min_child_weight'] = 4           #default: 1
    param['max_delta_step'] = 4             #default: 0
    param['subsample'] = 0.7                  #default: 1
    param['colsample_bytree'] = 0.7           #default: 1
    param['seed'] = 0
    num_rounds = 2500

    plst = list(param.items())

    data_train, data_cv, labels_train, labels_cv = train_test_split(X, y, test_size=0.20, random_state=42)

    xgtrain = xgb.DMatrix(data_train, label = labels_train)
    xgcv = xgb.DMatrix(data_cv, label = labels_cv)

    evallist = [(xgcv,'eval')]
    model = xgb.train(plst, xgtrain, num_rounds, evallist, early_stopping_rounds = 100)

    model.save_model('voice-gender.model')

train_df = pd.read_csv('../Data/voice.csv')

X = train_df.ix[:, 0:20]
y = train_df["label"]
y = y.replace({'male':1,'female':0})

runXGB(X, y)
