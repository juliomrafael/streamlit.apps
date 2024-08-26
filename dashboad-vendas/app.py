import streamlit as st
import pandas as pd
import altair as alt

#Título do dashboad
st.title('Supermercado SComar')

#Carregamento da base de dados
df = pd.read_csv('vendas_loja.csv')
#st.dataframe(df)

#Criando os filtros
regiao = st.sidebar.multiselect('Seleciona a Região: ', options = df['Região'].unique(), default=df['Região'].unique())

#Aplicando os filtros
if regiao:
    df_filtered = df[(df['Região'].isin(regiao))]
else:
    df_filtered = df

#Layout
coluna1, coluna2 = st.columns(2)
coluna3, coluna4 = st.columns(2)

with coluna1:
    #Gráfico de barras que apresenta as receitas por categoria de produtos
    st.subheader('Receita por Categoria de produtos')
    st.bar_chart(df_filtered.groupby('Categoria')['Receita'].sum())
with coluna2:
    #Gráfico de barras que apresenta as quantidade vendida por regiao
    st.subheader('Receita por Categoria de produtos')
    st.bar_chart(df_filtered.groupby('Região')['Quantidade_Vendida'].sum())

with coluna3:
    st.subheader('Receita ao Longo do Tempo')
    #Converter as datas de string para Date
    df['Data_Venda'] = pd.to_datetime(df_filtered['Data_Venda'])
    st.line_chart(df_filtered.groupby('Data_Venda')['Receita'].sum())

with coluna4:
    st.subheader('Quantidade Vendida vs Receita por Produto')
    scatter = alt.Chart(df_filtered).mark_circle(size=60).encode(
            x='Quantidade_Vendida',
            y='Receita',
            color='Categoria',
            tooltip=['Produto', 'Quantidade_Vendida', 'Receita']
            )
    st.altair_chart(scatter, use_container_width=True)
