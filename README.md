# PriceFit

House price least-squares model comparison (MAT2303 mini project).

Four models (M1–M4) are fitted to 20 houses using the normal equations (Gauss-Jordan), cross-checked with QR, and compared by RMSE, R², adjusted R² and leave-one-out error. All maths runs in plain JavaScript in the browser; Streamlit only serves the page.

## Files

| File | Purpose |
|---|---|
| `app.py` | Streamlit entry point, embeds the HTML app |
| `pricefit.html` | The full PriceFit app |
| `requirements.txt` | Python dependencies |
| `.streamlit/config.toml` | Optional theme and server settings |

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

1. Push this repo to GitHub.
2. Go to https://share.streamlit.io and sign in with GitHub.
3. Click **Create app**, pick this repo, branch `main`, main file `app.py`.
4. Click **Deploy**. You get a public `*.streamlit.app` link.
