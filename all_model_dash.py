import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

attribution_model = pd.read_csv('/content/All_Models.csv')

colors = {
    'background': '#000000',
    'text': '#23c41d',
    'linecolor': '#363434'
}

app.layout = html.Div(style={'backgroundColor': colors['background']},children=[
    html.H1(
      children='Attribution models',
      style={
            'textAlign': 'center',
            'color': colors['text']
        }
      ),

    html.H2(children="""
        Attribution Model Visualisation [DASH].
    """,
    style={
            'textAlign': 'center',
            'color': colors['text'],
            'font': 36
        }
    ),
    html.Div(
      dcc.Dropdown(
        id='attribution-model',
        options=[
          {'label': i, 'value': i} for i in attribution_model['Model'].unique()
        ],
        value= 'Model_Type'
      )
    ),
    dcc.Graph(id='model-graph'),
    html.Div(
      dcc.RadioItems(
        id='attribution-type',
    options=[
        {'label': 'ROI', 'value': 'roi'},
        {'label': 'Graphs', 'value': 'Graphs'}
    ],
    value='roi',
    labelStyle={'display': 'inline-block',
                'font-weight': 300
    },
    style={
      'color': colors['text'],
      'textAlign': 'center'
    }

    )
    )
])
@app.callback(
    Output('model-graph', 'figure'),
    [Input('attribution-model', 'value'),
     Input('attribution-type', 'value')]
)
def update_graph(model_name,model_type):
  dff = attribution_model[attribution_model['Model'] == model_name]
  if(model_type == 'roi' ):
    return {
      'data': [
        {'x': dff['0'],
        'y': dff['2'], 'type': 'bar', 'name': model_name, 'xlable': 'camp'},
        {'x': dff['0'],
        'y': dff['2'], 'type': 'linear', 'name': model_name},
        ],
        'layout': {
          'title': model_name,
          'plot_bgcolor': colors['linecolor'],
          'paper_bgcolor': colors['linecolor'],
          'xaxis':{'title':'Campaign ID'},
          'yaxis':{'title':'Return Of Investment%'},
          'font': {
            'color': colors['text']
            }
        }
    }
  else:
    return{
      'data': [
        {'x': dff['0'],
         'y': dff['1'], 'type': 'bar', 'name': model_name},
        {'x': dff['0'],
         'y': dff['1'], 'type': 'linear', 'name': model_name},
        ],
        'layout': {
          'title': model_name,
          'plot_bgcolor': colors['linecolor'],
          'paper_bgcolor': colors['linecolor'],
          'xaxis':{'title':'Campaign ID'},
          'yaxis':{'title':'Return Per Impression'},
          'font': {
            'color': colors['text']
          }
        }
    }

      


if __name__ == '__main__':
    app.run_server(debug=True)