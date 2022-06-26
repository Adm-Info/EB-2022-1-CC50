import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def showCatsBy(by,xlabel=''): #views
  if xlabel == '': xlabel = by 
  plt.figure(figsize=(16,8))
  plt.xticks(rotation=90)
  catplot = sns.boxplot(x="snippet.title", y=by, data=data_cat, palette='rainbow')
  catplot.set(title= xlabel +' por Categoría', ylabel="Categoría", xlabel=xlabel)

def outliersToMax(cat, since:int, col = 'views'):
  nCat = len(data_cat[data_cat['snippet.title'] == cat])
  nCatOut = len(data_cat[data_cat['snippet.title'] == cat][data_cat[col]>since])
  print( ' Cantidad de datos de entretainment:', nCat, '\n', 'Cantidad de datos outliers:', nCatOut )
  display(data_cat[data_cat['snippet.title'] == cat][data_cat[col]>since])
  print(f'''De {nCat} filas, {nCatOut} son outliers de la categoría entretainment.
    Estos serán ajustados al máximo menor a {since}.''')
  data_cat.loc[ (data_cat['snippet.title'] == cat) & (data_cat[col]>since), col ] = (
    data_cat[data_cat['snippet.title'] == cat ][data_cat[col]<since][col].max() )
  display(data_cat[data_cat['snippet.title'] == cat][data_cat[col]>since])



def correct_outliers_cats(col, q_min=0.025, q_max=0.95):
  outliers = data_cat.groupby('snippet.title').agg(
      out_min = (col, lambda x : x.quantile(q_min)),
      out_max = (col, lambda x : x.quantile(q_max))
    )
  outliers.reset_index(inplace=True)
  display(outliers)
  

  for index, row in outliers.iterrows():
    cat, omin, omax = row

    nCat = len(data_cat[data_cat['snippet.title'] == cat])
    nCatOutMax = len(data_cat[data_cat['snippet.title'] == cat][data_cat[col]>omax])
    nCatOutMin = len(data_cat[data_cat['snippet.title'] == cat][data_cat[col]<omin])
    print( f"{cat} por {col}".upper() )
    print( f'Frecuencia: {nCat} \t f. outliers min: {nCatOutMin} \t f. outliers max: {nCatOutMax}' )

    #corrigiendo outliers máximos
    if (nCatOutMax > 0):
      data_cat.loc[ (data_cat['snippet.title'] == cat) & (data_cat[col]>omax), col ] = [omax]*nCatOutMax
    #corrigiendo outliers mínimos
    if (nCatOutMin > 0):
      data_cat.loc[ (data_cat['snippet.title'] == cat) & (data_cat[col]<omin), col ] = [omin]*nCatOutMin
    
  