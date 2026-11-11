# Neural Network Activation Function Visualisers

Three **separate Streamlit applications** demonstrate the ReLU, Sigmoid and Tanh activation functions for BSD3513 Artificial Intelligence (Neural Networks lab).

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

- ReLU: [insert link]
- Sigmoid: [insert link]
- Tanh: [insert link]

## Validation

- ReLU(-2)=0, ReLU(2)=2
- Sigmoid(0)=0.5
- Tanh(0)=0

## Project files

- `common.py` — reusable activation mathematics and chart generation
- `relu_app.py`, `sigmoid_app.py`, `tanh_app.py` — independent Streamlit entry points
- `requirements.txt` — dependencies
- `screenshots/` — add screenshots of your three deployed applications

## Notes

These applications visualise activation functions; they do **not** train a neural network. The course PDF contains inconsistent lab numbering (Lab Report 5 on page 1 and Lab Report 4 on pages 3–4); confirm the correct filename with the lecturer.
