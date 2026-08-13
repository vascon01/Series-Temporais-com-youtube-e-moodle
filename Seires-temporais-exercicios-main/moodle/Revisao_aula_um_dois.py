import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.stattools import adfuller, kpss

# =============================================================================
# 1. DATASET 1: AirPassengers
# =============================================================================
print("--- PROCESSANDO AIRPASSENGERS ---")

# Carrega os dados
dado_um = sm.datasets.get_rdataset("AirPassengers", package="datasets").data

# Transformações
value = dado_um["value"]
value_um = np.log(value)           # Log para estabilizar a variância
value_dois = value_um.diff()       # 1ª Diferença (remover tendência)
value_tres = value_dois.diff(12)   # Diferença Sazonal de 12 períodos

# Teste ADF na série diferenciada
resultado_adf = adfuller(value_dois.dropna())
print(f"Estatística ADF (value_dois): {resultado_adf[0]:.4f}")
print(f"p-valor ADF (value_dois): {resultado_adf[1]:.4f}")

# Teste KPSS na série original (Corrigido: 'regression' com 'ss')
resultado_kpss = kpss(value, regression="c", nlags="auto")
print(f"Estatística KPSS (value): {resultado_kpss[0]:.4f}")
print(f"p-valor KPSS (value): {resultado_kpss[1]:.4f}")

# Opcional: Gráfico da série com dupla diferença
# plt.figure(figsize=(10, 4))
# plt.plot(value_tres)
# plt.title("AirPassengers - Log + Diferença Simples + Diferença Sazonal")
# plt.show()


# =============================================================================
# 2. DATASET 2: LakeHuron
# =============================================================================
print("\n--- PROCESSANDO LAKEHURON ---")

# Carrega os dados
dado_dois = sm.datasets.get_rdataset("LakeHuron", package="datasets").data

print("Primeiras linhas do dataset original:")
print(dado_dois.head())

# Ajuste do Índice de Anos (LakeHuron traz o tempo no 'time' ou no próprio 'index')
if "time" in dado_dois.columns:
    dado_dois.set_index("time", inplace=True)
elif "time" not in dado_dois.columns and dado_dois.index.name != "time":
    # Garante o intervalo histórico oficial do LakeHuron (1875 - 1972)
    dado_dois.index = pd.date_range(start="1875", periods=len(dado_dois), freq="YS").year
    dado_dois.index.name = "time"

print("\nDataset LakeHuron com índice ajustado:")
print(dado_dois.head())