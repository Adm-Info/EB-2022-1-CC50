import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def showCatsBy(by): #views
  print('ok')
  plt.figure(figsize=(16,8))
  plt.xticks(rotation=90)
  catplot = sns.boxplot(x="snippet.title", y=by, data=data_cat, palette='rainbow')
  catplot.set(title= by +' por categoría')

def outliersToMax(cat, since:int, col = 'views'):
  nCat = len(data_cat[data_cat['snippet.title'] == cat])
  nCatOut = len(data_cat[data_cat['snippet.title'] == cat][data_cat[col]>since])
  print( ' Cantidad de datos de entretainment:', nCat, '\n', 'Cantidad de datos outliers:', nCatOut )
  display(data_cat[data_cat['snippet.title'] == cat][data_cat[col]>since])
  print(f'''De {nCat} filas, {nCatOut} son outliers de la categoría entretainment.
    Estos serán ajustados al máximo menor a {since}.''')
  data_cat[col].loc[ (data_cat['snippet.title'] == cat) & (data_cat[col]>since)] = (
    data_cat[data_cat['snippet.title'] == cat ][data_cat[col]<since][col].max() )
  display(data_cat[data_cat['snippet.title'] == cat][data_cat[col]>since])
  