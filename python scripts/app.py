from pathlib import Path

from dash import Dash, dcc, html
import pandas as pd
import plotly.express as px

app = Dash(__name__)

csv_path = Path(__file__).resolve().parent.parent / "output" / "pink_morsels_sales.csv"
df = pd.read_csv(csv_path)

fig = px.line(df, x="date", y="Sales", color="region", title="Pink Morsels Sales")

app.layout = html.Div(
    children=[
        html.H1(children="Pink Morsels Sales"),
        html.Div(
            children="This is a dashboard that shows the sales of pink morsels by region and date."
        ),
        dcc.Graph(figure=fig),
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
