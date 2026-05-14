import pandas as pd

@app.get("/dados")
def dados():
    df = pd.read_excel("Base - Projetos Logistica 2026.xlsm", sheet_name="PORTFOLIO_LOGISTICA")
    return df.to_dict(orient="records")
@app.get("/dashboard")

def dashboard():
    df = pd.read_excel("Base - Projetos Logistica 2026.xlsm", sheet_name="PORTFOLIO_LOGISTICA")

    total = len(df)

    em_dia = df[df["Status"].str.contains("Em Dia", na=False)].shape[0]
    atencao = df[df["Status"].str.contains("Atenção", na=False)].shape[0]
    critico = df[df["Status"].str.contains("Crítico", na=False)].shape[0]

    return {
        "total": total,
        "em_dia": em_dia,
        "atencao": atencao,
        "critico": critico
    }
