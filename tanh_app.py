"""Standalone Streamlit application for Tanh activation."""
import streamlit as st
from common import activation, draw_chart

st.set_page_config(page_title='Tanh Visualiser', page_icon='📈', layout='wide')
st.title('Tanh Activation Function')
st.write('Hyperbolic tangent smoothly maps real-valued inputs into the interval (-1, 1).')
st.latex(r'\tanh(x)=\frac{e^x-e^{-x}}{e^x+e^{-x}}')
x = st.slider('Choose input x', -10.0, 10.0, 0.0, 0.1)
y = activation('Tanh', x)
st.metric('Tanh output', f'{y:.4f}')
st.plotly_chart(draw_chart('Tanh', x), use_container_width=True)
st.info('Tanh is zero-centred, but its gradient can become very small at large input magnitudes.')
