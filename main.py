from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# Libera acesso do frontend (GitHub Pages)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔹 DADOS COMPLETOS
@app.get("/dados")
def dados():
    df = pd.read_excel("Base - Projetos Logistica 2026.xlsm.xlsx", sheet_name="PORTFOLIO_LOGISTICA")
    return df.fillna("").to_dict(orient="records")


# 🔹 DASHBOARD
@app.get("/dashboard")
def dashboard():
    df = pd.read_excel("Base - Projetos Logistica 2026.xlsm.xlsx", sheet_name="PORTFOLIO_LOGISTICA")

    total = len(df)

    # Evita erro com valores nulos
    status_col = df["Status"].fillna("")

    em_dia = status_col.str.contains("Em Dia").sum()
    atencao = status_col.str.contains("Atenção").sum()
    critico = status_col.str.contains("Crítico").sum()

    return {
        "total": int(total),
        "em_dia": int(em_dia),
        "atencao": int(atencao),
        "critico": int(critico)
    }
