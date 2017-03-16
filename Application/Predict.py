import subprocess
import pandas as pd
import xgboost as xgb

subprocess.call ("/usr/bin/Rscript --vanilla /home/prathamsolanki/github/gender-recognition-by-voice/Application/ExtractFeatures.R", shell=True)

features_to_use = ["meanfreq","sd","median","Q25","Q75","IQR","skew","kurt","sp.ent","sfm","mode","centroid","meanfun","minfun","maxfun","meandom","mindom","maxdom","dfrange","modindx"]

test_df = pd.read_csv('../Data/Amy-Acoustics.csv')

test_X = test_df[features_to_use]
xgtest = xgb.DMatrix(test_X)

model = xgb.Booster({'nthread':4})
model.load_model("voice-gender.model")

pred_test_y = model.predict(xgtest)

if pred_test_y >= 0.5:
    print "male"

else:
    print "female"
