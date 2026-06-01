import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Leitura dos dados
df = pd.read_csv('ecommerce_estatistica.csv')

# Inicializa a aplicação
app = Dash(__name__)

# Histograma
fig_hist = px.histogram(
    df,
    x='Preço',
    title='Distribuição dos Preços'
)

# Dispersão
fig_disp = px.scatter(
    df,
    x='Preço',
    y='Nota',
    title='Preço x Nota'
)

# Mapa de calor
corr = df[['Preço', 'Nota', 'N_Avaliações', 'Desconto', 'Qtd_Vendidos_Cod']].corr()

fig_heat = px.imshow(
    corr,
    text_auto=True,
    title='Mapa de Calor das Correlações'
)

# Barras
marcas = df['Marca'].value_counts().head(10).reset_index()
marcas.columns = ['Marca', 'Quantidade']

fig_bar = px.bar(
    marcas,
    x='Marca',
    y='Quantidade',
    title='Top 10 Marcas'
)

# Pizza
temporadas = df['Temporada'].value_counts().head(5)

fig_pizza = px.pie(
    values=temporadas.values,
    names=temporadas.index,
    title='Distribuição por Temporada'
)

# Densidade
fig_densidade = px.density_contour(
    df,
    x='Preço',
    y='Nota',
    title='Densidade: Preço x Nota'
)

# Regressão
fig_reg = px.scatter(
    df,
    x='N_Avaliações',
    y='Qtd_Vendidos_Cod',
    trendline='ols',
    title='Relação entre Avaliações e Quantidade Vendida'
)

# Layout
app.layout = html.Div([
    html.H1(
        'Dashboard E-commerce',
        style={'textAlign': 'center'}
    ),

    dcc.Graph(figure=fig_hist),
    dcc.Graph(figure=fig_disp),
    dcc.Graph(figure=fig_heat),
    dcc.Graph(figure=fig_bar),
    dcc.Graph(figure=fig_pizza),
    dcc.Graph(figure=fig_densidade),
    dcc.Graph(figure=fig_reg)
])

# Executa aplicação
if __name__ == '__main__':
    app.run(debug=True)