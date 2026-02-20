# Importar librerías principales
import plotly.graph_objects as go
import numpy as np

def graficar_serie(
        original,
        forecast,
        title
):
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=original.index,
            y=original,
            mode='lines',
            name='Pasajeros reales',
            opacity=0.5
        )
    )

    fig.add_trace(
        go.Scatter(
            x=forecast.index,
            y=forecast,
            mode='lines',
            name=title
        )
    )

    fig.update_layout(
        title=title,
        xaxis_title='Fecha',
        yaxis_title='Número de pasajeros'
    )

    fig.show()

def mape(
    original,
    forecast
):
    
    mask = forecast.notna()

    mape = np.mean(
        np.abs(
            (original[mask] - forecast[mask]) / original[mask]
        )
    ) * 100

    return mape