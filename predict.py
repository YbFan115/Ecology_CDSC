# coding: utf-8
import rpy2.robjects as robjects
from rpy2.robjects.packages import SignatureTranslatedAnonymousPackage
r_code = '''
predict_func <- function(model, newdata) {
  predict(model, newdata, type = "response")
  }
  '''
r_wrapper = SignatureTranslatedAnonymousPackage(r_code, "r_wrapper")
r_model = robjects.r['readRDS']('good_wiki-reddit-mapping_logistic.RDS')
import pandas as pd
df = pd.read_csv("subred_fandom_features.csv")

from rpy2.robjects import pandas2ri
pandas2ri.activate()


predictions = r_wrapper.predict_func(r_model, df)
predictions
