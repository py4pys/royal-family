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

from app import app
from db import transforms


# reference
# https://dash.plotly.com/urls
# https://medium.com/@erickleppen/list/dash-and-plotly-tutorials-9713e02d180d

# database
conn = sqlite3.connect("db/python_dev.sqlite")
c = conn.cursor()

# boilerplate
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], use_pages=True)
server = app.server
app.config.suppress_callback_exceptions = True




if __name__ == "__main__":
    app.run_server()