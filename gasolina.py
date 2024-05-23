import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados_gasolina = pd.read_csv('gasolina.csv')

with sns.axes_style('whitegrid'):

  grafico_gasolina = sns.lineplot(data=dados_gasolina, x="dia", y="venda")
  grafico_gasolina.set(title='Preço médio da gasolina em São Paulo nos 10 primeiros dias de Julho de 2021', xlabel='Dia', ylabel='Preço');

plt.savefig('gasolina.png')