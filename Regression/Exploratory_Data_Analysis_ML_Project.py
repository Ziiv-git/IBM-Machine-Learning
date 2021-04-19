### Importing the packages
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter as FF
from matplotlib.ticker import StrMethodFormatter as SMF
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression as LR
from sklearn.feature_selection import f_regression as fr

### Reading in the dataframe
df = pd.read_csv('https://raw.githubusercontent.com/ultimatist/DDS/master/data/Ames_Housing_Data.tsv', sep='\t')
df.head()

########### DATA EXPLORATION ##############
### Finding the missing values
df_na = df.isna().sum().to_frame().sort_values(by = 0, axis = 0)
df_na.rename(columns={0: 'NA Count'}, inplace=True)
df_na[df_na['NA Count'] == 0].index

###############################################3
### Exploration 1: Price vs Lot Area and Number Of Bedrooms
#Scatter Plot.
exp1 = sns.lmplot(data = df, x = 'Lot Area', y = 'SalePrice', hue = 'Bedroom AbvGr',
                  palette = 'viridis_r', ci = None, height = 6, aspect = 13 / 6)

#Axes.
ax = plt.gca()

#Title setup.
ax.set_title('Price vs Lot Area and Number of Bedrooms', fontsize = 24)

#X-axis setup.
ax.set_xlabel("Lot Area (sq. ft.)", fontsize = 22)
ax.set_xscale('log')
xlabels = [2500, 5000, 10000, 25000, 50000, 100000, 250000]
ax.set_xticks(xlabels)
ax.set_xticklabels(xlabels, rotation = 45, ha = 'right')
ax.get_xaxis().set_major_formatter(FF(lambda x, p: format(int(x), ',')))

#Y-axis setup.
ax.set_ylabel("Price", fontsize = 22)
ax.set_ylim(0, 800000)
ax.yaxis.set_major_formatter(SMF('${x:,.0f}'))

ax.tick_params(axis = 'both', which = 'major', labelsize = 14)

#Legend setup.
exp1._legend.remove()
ax.legend(loc = 'upper left', title = 'Bedrooms', ncol = 2, title_fontsize = 18, fontsize = 14)


#### Finding count distribution of number of bedrooms
bdrm_cnt = df['Bedroom AbvGr'].value_counts().sort_index().to_frame().rename(columns = {'Bedroom AbvGr': "Count of Houses"})
bdrm_cnt.index.name = "Number of Bedrooms"
bdrm_cnt

##################################################
### Exploration 2: Violin plot of Price vs Neighborhood
#Sort Neighborhoods by median Price in ascending order.
xlabels = df.groupby(['Neighborhood'])['SalePrice'].median().sort_values().index

exp2 = sns.violinplot(data = df, x = 'Neighborhood', y = 'SalePrice', scale = 'width', width = 0.6,
                      palette = 'viridis_r', order = xlabels)

plt.gcf().set_size_inches(15, 6.92)

#Axes.
ax = plt.gca()

#Title setup.
ax.set_title('Price vs Neighborhood', fontsize = 24)

#X-axis setup.
ax.set_xlabel("Neighborhood", fontsize = 22)
ax.set_xticklabels(ax.get_xticklabels(), rotation = 45, ha = 'right')

#Y-axis setup.
ax.set_ylabel("Price", fontsize = 22)
ax.set_ylim(0, 800000)
ax.yaxis.set_major_formatter(SMF('${x:,.0f}'))

ax.tick_params(axis = 'both', which = 'major', labelsize = 14)

###########################################################
### Exploration 3: Price vs Year Built and Overall Quality
#Scatter Plot.
exp3 = sns.lmplot(data = df, x = 'Year Built', y = 'SalePrice', hue = 'Overall Qual',
                  palette = 'viridis_r', ci = None, height = 6, aspect = 13 / 6)

#Axes.
ax = plt.gca()

#Title setup.
ax.set_title('Price vs Year Built and Overall Quality', fontsize = 24)

#X-axis setup.
ax.set_xlabel("Year Built", fontsize = 22)
ax.set_xlim(1870, 2015)
ax.set_xticklabels(ax.get_xticklabels(), rotation = 45, ha = 'right')

#Y-axis setup.
ax.set_ylabel("Price", fontsize = 22)
ax.set_ylim(0, 800000)
ax.yaxis.set_major_formatter(SMF('${x:,.0f}'))

ax.tick_params(axis = 'both', which = 'major', labelsize = 14)

#Legend setup.
exp3._legend.remove()
ax.legend(loc = 'upper left', title = 'Overall House Quality',
          labels = ['Very Poor', 'Poor', 'Fair', 'Below Average', 'Average',
                    'Above Average', 'Good', 'Very Good', 'Excellent', 'Very Excellent'],
          ncol = 2, title_fontsize = 18, fontsize = 14)


############## HYPOTHESIS TESTING ##################
### Significance Test
x = df['Overall Qual'].to_numpy().reshape(-1, 1)
y = df['SalePrice'].to_numpy().reshape(-1, )
reg = LR().fit(x, y)
r_sq = reg.score(x, y)
p_val = fr(x, y)[1][0]

print("The R-squared is {}.".format(round(r_sq, 3)))
print("The p_value is {}.".format(p_val))
