from dash import Dash, html

app = Dash(__name__)
server = app.server 

PROJECT_TITLE = "Movie Similarity Explorer for Neurodiversity"

# TODO: replace these with the REAL Render URLs
URL_FEATURE = "https://neurodiversity-friendly-movie-explorer.onrender.com"
URL_EMOTION = "https://finalproject-viz.onrender.com"

app.layout = html.Div(
    style={
        "fontFamily": "Arial, sans-serif",
        "minHeight": "100vh",
        "backgroundColor": "#f3f4f6",
        "display": "flex",
        "alignItems": "center",
        "justifyContent": "center",
        "padding": "32px",
    },
    children=[
        html.Div(
            style={
                "backgroundColor": "white",
                "borderRadius": "18px",
                "padding": "32px 40px",
                "boxShadow": "0 15px 35px rgba(0,0,0,0.1)",
                "maxWidth": "900px",
                "width": "100%",
                "textAlign": "center",
            },
            children=[
                html.H1(
                    PROJECT_TITLE,
                    style={"marginBottom": "10px", "fontSize": "26px"},
                ),
                html.P(
                    "This project combines two complementary visualizations: "
                    "a feature-based network explorer and an emotional similarity explorer.",
                    style={"color": "#4b5563", "fontSize": "14px", "marginBottom": "28px"},
                ),

                html.Div(
                    style={
                        "display": "flex",
                        "gap": "20px",
                        "justifyContent": "center",
                        "flexWrap": "wrap",
                    },
                    children=[
                        # version A (feature-based)
                        html.A(
                            href=URL_FEATURE,
                            target="_blank",
                            children=html.Div(
                                [
                                    html.Div(
                                        "Feature-Based Similarity Explorer",
                                        style={
                                            "fontWeight": "bold",
                                            "fontSize": "18px",
                                            "marginBottom": "6px",
                                        },
                                    ),
                                    html.Div(
                                        "Network view using genre & tag features; calm and detailed modes.",
                                        style={"fontSize": "13px", "color": "#4b5563"},
                                    ),
                                ]
                            ),
                            style={
                                "textDecoration": "none",
                                "backgroundColor": "#e5f0ff",
                                "padding": "20px 24px",
                                "borderRadius": "14px",
                                "minWidth": "260px",
                                "boxShadow": "0 8px 20px rgba(37, 99, 235, 0.25)",
                                "border": "1px solid #bfdbfe",
                                "color": "#1d4ed8",
                                "display": "inline-block",
                            },
                        ),

                        # version B (emotion-based)
                        html.A(
                            href=URL_EMOTION,
                            target="_blank",
                            children=html.Div(
                                [
                                    html.Div(
                                        "Emotional Similarity Explorer",
                                        style={
                                            "fontWeight": "bold",
                                            "fontSize": "18px",
                                            "marginBottom": "6px",
                                        },
                                    ),
                                    html.Div(
                                        "NRC-VAD emotional space with multiple interactive views.",
                                        style={"fontSize": "13px", "color": "#4b5563"},
                                    ),
                                ]
                            ),
                            style={
                                "textDecoration": "none",
                                "backgroundColor": "#fef3c7",
                                "padding": "20px 24px",
                                "borderRadius": "14px",
                                "minWidth": "260px",
                                "boxShadow": "0 8px 20px rgba(245, 158, 11, 0.25)",
                                "border": "1px solid #fcd34d",
                                "color": "#b45309",
                                "display": "inline-block",
                            },
                        ),
                    ],
                ),

                html.P(
                    "Click a card to open each version in a new tab. "
                    "Both visualizations together form our final project.",
                    style={
                        "marginTop": "26px",
                        "fontSize": "12px",
                        "color": "#6b7280",
                    },
                ),
            ],
        )
    ],
)

if __name__ == "__main__":
    app.run(debug=True)
