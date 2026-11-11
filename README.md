# Neural Network Activation Function Visualisers

Three **separate Streamlit applications** demonstrate the ReLU, Sigmoid and Tanh activation functions for BSD3513 Artificial Intelligence (Neural Networks lab).

🔗 Project Links

GitHub Repository: https://github.com/hasnurhisham/Neural_Network.git

## Applications

| Application | Run command | Formula | Range |
|---|---|---|---|
| ReLU | `streamlit run relu_app.py` | max(0, x) | [0, ∞) |
| Sigmoid | `streamlit run sigmoid_app.py` | 1 / (1 + exp(-x)) | (0, 1) |
| Tanh | `streamlit run tanh_app.py` | tanh(x) | (-1, 1) |

Each app has a slider, calculated output, an interactive Plotly curve, and a highlighted point showing the selected input.

## Setup

```bash
python3 -m pip install -r requirements.txt
python3 -m streamlit run relu_app.py
```

Stop the running app and replace `relu_app.py` with `sigmoid_app.py` or `tanh_app.py` to run the other applications.

## Deployment

Create **three separate Streamlit Community Cloud deployments**, all pointing to the same GitHub repository but using different main file paths (`relu_app.py`, `sigmoid_app.py`, `tanh_app.py`). Add each public URL to your lab report.

- ReLU: https://relu-neuralnetwork-lab4.streamlit.app
- Sigmoid: https://sigmoid-neuralnetwork-lab4.streamlit.app 
- Tanh:  https://tanh-neuralnetwork-lab4.streamlit.app

## Validation

- ReLU(-2)=0, ReLU(2)=2
- Sigmoid(2)=0.8808
- Tanh(2)=0.9640

