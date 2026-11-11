"""Standalone Streamlit application for Sigmoid activation."""
import streamlit as st
from common import activation, draw_chart

st.set_page_config(page_title='Sigmoid Visualiser', page_icon='📈', layout='wide')
st.title('Sigmoid Activation Function')
st.write('Sigmoid smoothly maps real-valued inputs into the interval (0, 1).')
st.latex(r'\sigma(x)=\frac{1}{1+e^{-x}}')
x = st.slider('Choose input x', -10.0, 10.0, 0.0, 0.1)
y = activation('Sigmoid', x)
st.metric('Sigmoid output', f'{y:.4f}')
st.plotly_chart(draw_chart('Sigmoid', x), use_container_width=True)
st.info('Sigmoid is useful for binary classification outputs. Its gradient becomes very small for large positive or negative inputs.')
