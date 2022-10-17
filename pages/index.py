import sqlite3

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output
import numpy as np
import pandas as pd
import plotly.graph_objects as go


dash.register_page(__name__, path="/", title="Home", name="home")

# database
conn = sqlite3.connect("db/python_dev.sqlite")
c = conn.cursor()

# boilerplate
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
app.config.suppress_callback_exceptions = True




if __name__ == "__main__":
    app.run_server()