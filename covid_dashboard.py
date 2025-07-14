import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# ✅ Load data directly from the web (no need to upload CSV)
url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
df = pd.read_csv(url)
df = df[df['continent'].notna()]

# ✅ Initialize Dash app
app = Dash(__name__)
server = app.server  # Required for Render

# ✅ App layout
app.layout = html.Div([
    html.H1("🌍 COVID-19 Global Dashboard", style={'textAlign': 'center'}),

    html.Label("Select a Country:", style={'fontSize': 18}),
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': c, 'value': c} for c in sorted(df['location'].unique())],
        value='United States',
        style={'width': '60%'}
    ),

    html.Br(),
    dcc.Graph(id='cases-line-chart'),
    dcc.Graph(id='deaths-line-chart'),
    dcc.Graph(id='vaccination-line-chart'),
])

# ✅ Interactive updates
@app.callback(
    Output('cases-line-chart', 'figure'),
    Output('deaths-line-chart', 'figure'),
    Output('vaccination-line-chart', 'figure'),
    Input('country-dropdown', 'value')
)
def update_charts(selected_country):
    country_df = df[df['location'] == selected_country]

    fig_cases = px.line(country_df, x='date', y='new_cases',
                        title=f'Daily COVID-19 Cases in {selected_country}')
    fig_deaths = px.line(country_df, x='date', y='new_deaths',
                         title=f'Daily COVID-19 Deaths in {selected_country}')
    fig_vacc = px.line(country_df, x='date', y='people_vaccinated',
                       title=f'Cumulative Vaccinations in {selected_country}')

    return fig_cases, fig_deaths, fig_vacc

# ✅ Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
