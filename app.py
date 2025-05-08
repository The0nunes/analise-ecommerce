import pandas as pd
import dash
from dash import dcc, html
import plotly.express as px

# Ler os dados
df = pd.read_csv('ecommerce_estatistica.csv')

# Inicializar o app Dash
app = dash.Dash(__name__)
app.title = "Dashboard E-commerce"

# Gráfico 1 - Histograma de Preços
hist_preco = px.histogram(df, x='Preço', nbins=20, title='Distribuição de Preços')

# Gráfico 2 - Dispersão Preço vs Avaliação
scatter_preco_avaliacao = px.scatter(df, x='Preço', y='Nota', title='Preço vs Nota', opacity=0.5)

# Gráfico 3 - Barras por Categoria
material_counts = df['Material'].value_counts().reset_index()
material_counts.columns = ['Material', 'Count']

bar_categoria = px.bar(material_counts, x='Material', y='Count', title='Quantidade por Material')


# Layout da aplicação
app.layout = html.Div(children=[
    html.H1("Dashboard de Análise de E-commerce", style={'textAlign': 'center'}),
    
    dcc.Graph(figure=hist_preco),
    dcc.Graph(figure=scatter_preco_avaliacao),
    dcc.Graph(figure=bar_categoria)
])

# Rodar o servidor
if __name__ == '__main__':
    app.run(debug=True)

