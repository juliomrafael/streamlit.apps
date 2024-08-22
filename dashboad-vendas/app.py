import streamlit as st
import pandas as pd
import altair as alt

#Título do dashboad
st.title('Supermercado SComar')

#Carregamento da base de dados
df = pd.read_csv('vendas_loja.csv')
#st.dataframe(df)

#Gráfico de barras que apresenta as receitas por categoria de produtos
st.subheader('Receita por Categoria de produtos')
st.bar_chart(df.groupby('Categoria')['Receita'].sum())

#Gráfico de barras que apresenta as quantidade vendida por regiao
st.subheader('Receita por Categoria de produtos')
st.bar_chart(df.groupby('Região')['Quantidade_Vendida'].sum())