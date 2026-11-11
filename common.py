"""Shared mathematical functions and plotting utilities for activation demos."""
import numpy as np
import plotly.graph_objects as go


def activation(name: str, x):
    """Evaluate an activation function for a scalar or NumPy array."""
    a = np.asarray(x, dtype=float)
    if name == 'ReLU':
        y = np.maximum(0, a)
    elif name == 'Sigmoid':
        y = np.where(a >= 0, 1 / (1 + np.exp(-np.abs(a))), np.exp(-np.abs(a)) / (1 + np.exp(-np.abs(a))))
    elif name == 'Tanh':
        y = np.tanh(a)
    else:
        raise ValueError(f'Unknown activation: {name}')
    return float(y) if y.ndim == 0 else y


def draw_chart(name: str, selected_x: float):
    xs = np.linspace(-10, 10, 601)
    ys = activation(name, xs)
    selected_y = activation(name, selected_x)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=xs, y=ys, mode='lines', name=name, line=dict(width=3)))
    fig.add_trace(go.Scatter(x=[selected_x], y=[selected_y], mode='markers', name='Selected input', marker=dict(size=13, color='#E75A59')))
    fig.add_hline(y=0, line_width=1, line_dash='dot', line_color='gray')
    fig.add_vline(x=0, line_width=1, line_dash='dot', line_color='gray')
    fig.update_layout(title=f'{name} activation function', xaxis_title='Input (x)', yaxis_title='Output f(x)', template='plotly_white', height=460, margin=dict(l=20,r=20,t=55,b=20))
    return fig
