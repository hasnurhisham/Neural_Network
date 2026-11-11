"""Standalone Streamlit application for ReLU activation."""
import streamlit as st
from common import activation, draw_chart

st.set_page_config(page_title='ReLU Visualiser', page_icon='📈', layout='wide')
st.title('ReLU Activation Function')
st.write('Rectified Linear Unit outputs zero for negative inputs and passes positive inputs unchanged.')
st.latex(r'f(x)=\max(0,x)')
x = st.slider('Choose input x', -10.0, 10.0, 2.0, 0.1)
y = activation('ReLU', x)
st.metric('ReLU output', f'{y:.4f}')
st.plotly_chart(draw_chart('ReLU', x), use_container_width=True)
st.info('ReLU is computationally simple and commonly used in hidden layers. Its derivative is zero for negative inputs, which can cause inactive neurons.')
