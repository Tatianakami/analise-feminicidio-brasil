import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# ler dados
df = pd.read_csv('dados/dados_tratados.csv')

# conferindo nomes das colunas
print(df.columns)

# renomeando para padronizar (se precisar)
df = df.rename(columns={
    'período': 'Ano',
    'valor': 'Taxa Feminicídio',
    'Estado': 'Estado'
})

# análise descritiva
print("\nAnálise Descritiva:\n", df.describe())

# Evolução da taxa por ano e estado
plt.figure(figsize=(12,6))
sns.lineplot(data=df, x='Ano', y='Taxa Feminicídio', hue='Estado')
plt.title('Evolução da Taxa de Feminicídio por Estado')
plt.xlabel('Ano')
plt.ylabel('Taxa por 100 mil mulheres')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Top 5 estados com maiores taxas no último ano disponível
ano_max = df['Ano'].max()
df_ultimo_ano = df[df['Ano'] == ano_max]
top5 = df_ultimo_ano.sort_values(by='Taxa Feminicídio', ascending=False).head(5)

fig = px.bar(top5, x='Estado', y='Taxa Feminicídio',
             title=f'Top 5 Estados com Maior Taxa de Feminicídio em {ano_max}',
             color='Estado', text='Taxa Feminicídio')
fig.show()
