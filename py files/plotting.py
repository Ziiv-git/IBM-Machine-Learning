# scatterplot
plt.plot(data.sepal_length, data.sepal_width, ls='', marker='o', label='sepal')

# histogram
plt.hist(data.sepal_length, bins=25)

# customising plots
fig, ax = plt.subplots()

# horizontal barplot
ax.barh(np.arange(10), data.sepal_width.iloc[:10])

# set position of ticks
ax.set_yticks(np.arange(0.4,10.4,1.0))
ax.set_yticklabels(np.arange(1,11))
ax.set(xlabel='xlabel', ylabel='ylabel', title='Title')

data.groupby('species').mean().plot(color=['red', 'blue', 'black', 'green'],
fontsize=10.0, figsize=(4,4))

# feature correlations
sns.pairplot(data, hue='species', size=3)

# hexbin plots
sns.jointplot(x=data['sepal_length'], y=data['sepal_width'], kind='hex')

#face grid
plot = sns.FaceGrid(data, col='species', margin_titles=True)
plot.map(plt.hist, 'sepal_length', color='green')
