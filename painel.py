from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

#inicializando programa
app = Dash(__name__)


# Base de dados ⬇
df = pd.read_excel("Vendas.xlsx")
fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
#Criação dos graficos ⬇
opcoes= list(df['ID Loja'].unique())
opcoes.append("Todas as lojas")

#componentes do html ⬇
app.layout = html.Div(children=[
    html.H1(children='Faturamento das lojas'),
    html.H1(children='Grafico com o faturamento de todos os produtos separados por loja'),

    html.Div(children='''
        OBS: Esse grafico mostra a quantidade de produtos vendidos, não o fturamento.
    '''),
    
#Componentes do dash ⬇
    dcc.Dropdown(opcoes, value='Todas as lojas', id='Lista-lojas'),
    dcc.Graph(
        id='grafico-quantidade-vendas',
        figure=fig
    )
])
@app.callback(
    Output('grafico-quantidade-vendas', 'figure'),
    Input('Lista-lojas', 'value')
)
def update_output(value):
    if value== "Todas as lojas":
        fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    else: 
        tabela_filtrada = df.loc[df['ID Loja']==value, :]
        fig = px.bar(tabela_filtrada, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    return fig


if __name__ == '__main__':
    app.run(debug=True)