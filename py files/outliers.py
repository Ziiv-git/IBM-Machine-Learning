# using plots
sns.distplot()


# using statistics
import numpy as np
# calculate interquartile range
q25, q50, q75 = np.percentile(data, [25, 50, 75])
iqr = q75 - q25
# calculate min/max limits to be considered an outlier
min = q25 - 1.5*iqr
max = q75 + 1.5*iqr
print(min, q25, q50, q75, max)
# identifying outliers
[x for x in data['Unemployment'] id x > max]


# using residuals (difference between actual and predicted values of the outcome variable)
# standardised approach (residual divided by standard error)
# deleted (observing the model after deleting the outlier)
# studentized (deleted residuals divided by residual standard error)
