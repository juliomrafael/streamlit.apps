import pandas as pd
import streamlit as st
import altair as alt

# Carregar o dataset
df = pd.read_csv('vendas_loja.csv')

#Extender a largura 
st.set_page_config(layout="wide")

# Título do dashboard
st.title('Dashboard de Vendas - Loja Online')

# Filtros na barra lateral
categoria = st.sidebar.multiselect('Selecione a Categoria:', options=df['Categoria'].unique(), default=df['Categoria'].unique())
regiao = st.sidebar.multiselect('Selecione a Região:', options=df['Região'].unique(), default=df['Região'].unique())

# Aplicando os filtros (caso algum filtro seja aplicado)
if categoria or regiao:
    df_filtered = df[(df['Categoria'].isin(categoria)) & (df['Região'].isin(regiao))]
else:
    df_filtered = df

# Layout de colunas
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

# Visualização 1: Receita Total por Categoria
with col1:
    st.subheader('Receita Total por Categoria')
    st.bar_chart(df_filtered.groupby('Categoria')['Receita'].sum())

# Visualização 2: Quantidade Vendida por Região
with col2:
    st.subheader('Quantidade Vendida por Região')
    st.bar_chart(df_filtered.groupby('Região')['Quantidade_Vendida'].sum())

# Visualização 3: Receita ao Longo do Tempo
with col3:
    st.subheader('Receita ao Longo do Tempo')
    df_filtered['Data_Venda'] = pd.to_datetime(df_filtered['Data_Venda'])
    receita_por_dia = df_filtered.groupby('Data_Venda')['Receita'].sum()
    st.line_chart(receita_por_dia)

# Visualização 4: Quantidade Vendida vs Receita por Produto
with col4:
    st.subheader('Quantidade Vendida vs Receita por Produto')
    scatter = alt.Chart(df_filtered).mark_circle(size=60).encode(
        x='Quantidade_Vendida',
        y='Receita',
        color='Categoria',
        tooltip=['Produto', 'Quantidade_Vendida', 'Receita']
    )
    st.altair_chart(scatter, use_container_width=True)
