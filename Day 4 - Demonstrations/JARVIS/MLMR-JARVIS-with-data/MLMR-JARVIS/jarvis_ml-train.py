#from jarvis.sklearn.get_desc import get_comp_descp
from monty.serialization import loadfn, MontyDecoder,dumpfn
import numpy as np
from sklearn.metrics import mean_absolute_error,r2_score,mean_squared_error
import lightgbm as lgb
import matplotlib.pyplot as plt
plt.switch_backend('agg')
import pandas as pd
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split,learning_curve,cross_val_score,cross_val_predict,GridSearchCV,RandomizedSearchCV
import scipy as sp
import time,os,json,pprint
from sklearn.feature_selection import SelectKBest,f_classif,SelectFromModel,VarianceThreshold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


# Download descriptors and material data from the following link:
#  https://figshare.com/articles/JARVIS-ML-CFID-descriptors_and_material_properties/6870101 

# Websites: https://www.ctcms.nist.gov/jarvisml, https://jarvis.nist.gov
# https://arxiv.org/abs/1805.07325


# NIST-disclaimer: https://www.nist.gov/disclaimer

#collection of functions
def isfloat(value):
  try:
    float(value)
    return True
  except :
    return False
    pass

#Get data and descriptors for a particular properties
def jdata(data_file='cfid_jarvisml_test_set.json',prop=''):
  d3=loadfn(data_file,cls=MontyDecoder)
  X=[]
  Y=[]
  jid=[]
  for ii,i in enumerate(d3):
    y=i[prop]
    if isfloat(y):
      y=float(y)
      x=i['desc']
      if len(x)==1557 and any(np.isnan(x) for x in x.flatten())==False:
        if 'eps' in prop:
          y=np.sqrt(float(y))
        if 'mag' in prop:
           num=get_number_formula_unit(i['strt'])
           y=float(abs(y))/float(num)
        X.append(x)
        Y.append(y)
        jid.append(i['jid'])
  print ('Prop=',prop,len(X),len(Y))
  X=np.array(X).astype(np.float64)
  Y=np.array(Y).astype(np.float64)
  return X,Y,jid

def regr_scores(pred,test):
   rmse=np.sqrt(mean_squared_error(test, pred))
   r2=r2_score(test, pred)
   mae=(mean_absolute_error(test, pred))
   info={}
   info['mae']=mae
   info['rmse']=rmse
   info['r2']=r2
   info['test']=test
   info['pred']=pred
   return info



if __name__ == '__main__':

  dat_3d=loadfn('cfid_jarvisml_test_set.json',cls=MontyDecoder)
  x,y,jid=jdata(prop='form_enp')
  X_train, X_test, y_train, y_test,jid_train,jid_test = train_test_split(x, y,jid, random_state=1, test_size=0.1)
  print (len(X_train), len(X_test))
  model = lgb.LGBMRegressor(
                    n_estimators=100,
                    learning_rate=0.1,
                    max_depth=5,
                    num_leaves=100,
                    objective='regression',
                    n_jobs=-1,
                    verbose=-1
                   )
  model.fit(X_train,y_train)
  pred=model.predict(X_test)
  reg_sc=regr_scores(y_test,pred)
  print (reg_sc)
