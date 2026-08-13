import yfinance as yf
from statsmodels.tsa.stattools import adfuller

dados = yf.download(
"^BVSP",
start="2010-01-01",
end="2025-12-31",
auto_adjust=True,
progress=False
)

# 1. Baixe os dados de uma ação (ex: PETR4.SA)
dados = yf.download("PETR4.SA", start="2023-01-01")

# 2. Agora a variável 'dados' existe no código
y = dados["Close"]
serie = y.dropna()

resultado = adfuller(serie)
print(f"p-valor: {resultado[1]:.4f}")