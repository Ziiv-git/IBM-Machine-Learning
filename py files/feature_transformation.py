# imports
from numpy import log, log1p
from scipy.stats import boxcox

#log transformation for +vely skewed
import math
log_data = [math.log(d) for d in data['Unemployment']]

# polynomial features
from sklearn.preprocessing import PolynomialFeatures
# create an instance of the class
polyFeat = PolynomialFeatures(degrees=2)
# create the polynomial features anf then transform the data
polyFeat = polyFeat.fit(x_data)
x_poly = polyFeat.transform(x_data)

# feature scaling
# for continuous features
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler
# for nominal features
from sklearn.preprocessing import LabelEncoder, LabelBinarizer, OneHotEncoder
from pandas import get_dummies
# for ordinal features
from sklearn.preprocessing import OrdinalEncoder
from sklearn.feature_extraction import DictVectorizer
