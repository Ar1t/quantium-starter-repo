from pathlib import Path

from dash import Dash, Input, Output, dcc, html
import pandas as pd
import plotly.express as px

app = Dash(__name__)

csv_path = Path(__file__).resolve().parent.parent / "output" / "pink_morsels_sales.csv"
df = pd.read_csv(csv_path)

regions = sorted(df["region"].unique())

app.layout = html.Div(
    children=[
        html.H1(children="Pink Morsels Sales"),
        html.Div(children="Filter sales by region:"),
        dcc.RadioItems(
            id="region-filter",
            options=[{"label": "All regions", "value": "all"}]
            + [{"label": r.title(), "value": r} for r in regions],
            value="all",
            inline=True,
            labelStyle={"marginRight": "20px"},
        ),
        dcc.Graph(id="sales-graph"),
    ]
)


@app.callback(
    Output("sales-graph", "figure"),
    Input("region-filter", "value"),
)
def update_graph(selected_region):
    if selected_region == "all":
        filtered = df
    else:
        filtered = df[df["region"] == selected_region]

    return px.line(
        filtered,
        x="date",
        y="Sales",
        color="region" if selected_region == "all" else None,
        title="Pink Morsels Sales",
    )


if __name__ == "__main__":
    app.run(debug=True)
