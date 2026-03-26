import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

def get_data():
    try:
        data = []
        with open("audits.log", "r") as f:
            for line in f:
                if "username:" in line and "password:" in line:
                    try:
                        user = line.split("username:")[1].split(",")[0].strip()
                        pwd = line.split("password:")[1].strip()
                        data.append({"Username": user, "Password": pwd})
                    except:
                        continue
        return pd.DataFrame(data)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Username", "Password"])


def update_layout():
    df = get_data()
    if df.empty:
        return html.Div("No data captured yet.")
    
    fig = px.histogram(df, x="Username", title="Most Targeted Usernames")
    
    return html.Div([
        html.H1("Honeypot Threat Intelligence Dashboard"),
        dcc.Graph(figure=fig)
    ])
app.layout = update_layout

if __name__ == '__main__':
    app.run(debug=True, port=8050)