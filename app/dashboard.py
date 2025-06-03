import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.title("Análise da Taxa de Feminicídio no Brasil por Estado")

# Carregar dados tratados
df = pd.read_csv('dados/dados_tratados.csv')

# Mostrar dados na tabela
st.subheader("Tabela dos dados")
st.dataframe(df)

# Evolução da taxa ao longo dos anos por estado
st.subheader("Evolução da Taxa de Feminicídio por Estado")
plt.figure(figsize=(12,6))
sns.lineplot(data=df, x='Ano', y='Taxa Feminicídio', hue='estado')
plt.xlabel('Ano')
plt.ylabel('Taxa por 100 mil mulheres')
plt.legend(loc='upper left', bbox_to_anchor=(1,1))
st.pyplot(plt)

# Top 5 estados no último ano disponível
st.subheader("Top 5 Estados com Maior Taxa no Último Ano")
ano_max = df['Ano'].max()
df_ultimo_ano = df[df['Ano'] == ano_max]
top5 = df_ultimo_ano.sort_values(by='Taxa Feminicídio', ascending=False).head(5)

fig = px.bar(top5, x='estado', y='Taxa Feminicídio',
             color='estado', text='Taxa Feminicídio',
             title=f'Top 5 Estados com Maior Taxa em {ano_max}')
st.plotly_chart(fig)







