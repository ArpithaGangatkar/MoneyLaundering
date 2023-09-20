from sklearn.exceptions import InconsistentVersionWarning
import warnings
import xgboost
import pickle
warnings.simplefilter("error", InconsistentVersionWarning)

model_path = 'saved_model/DecisionTree/DecisionTree.pickle'
model_path = 'EDA\PredictModel.pickle'
try:
    pass
   #est = pickle.loads(r'saved_model/DecisionTree/DecisionTree.pickle')
except InconsistentVersionWarning as w:
   print(w.original_sklearn_version)

with open(model_path,'rb') as f:
    mp= pickle.load(f)