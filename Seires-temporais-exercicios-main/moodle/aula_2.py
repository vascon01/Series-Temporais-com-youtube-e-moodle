import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Carregar dados
dado = sm.datasets.get_rdataset("AirPassengers", package="datasets").data

# 2. Transformações
dado_log = np.log(dado["value"])
dado_estacionario = dado_log.diff().dropna()

# Ajusta a coluna de tempo para alinhar com o dado diferenciado (remove o primeiro ano/mês)
tempo_diferenciado = dado["time"].iloc[1:]

# 3. Testes de Estacionariedade (ADF)
def interpretar_adf(serie, nome):
    resultado = adfuller(serie)
    p_valor = resultado[1]
    print(f"--- Teste ADF: {nome} ---")
    print(f"Estatística ADF: {resultado[0]:.4f}")
    print(f"p-valor: {p_valor:.4f}")
    if p_valor < 0.05:
        print("-> A série É ESTACIONÁRIA (rejeita H0 com 95% de confiança)\n")
    else:
        print("-> A série NÃO É ESTACIONÁRIA (não rejeita H0)\n")

interpretar_adf(dado["value"], "Série Original")
interpretar_adf(dado_estacionario, "Série Log + Diferenciada")

# 4. Visualização dos Gráficos
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(dado["time"], dado["value"], color="red")
plt.title("Série Original (Não Estacionária)")
plt.xlabel("Ano")
plt.ylabel("Passageiros")
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(tempo_diferenciado, dado_estacionario, color="blue")
plt.axhline(0, color="black", linestyle="--", linewidth=0.8)
plt.title("Série Transformed: Log + Diff (Estacionária)")
plt.xlabel("Ano")
plt.ylabel("Variação Log")
plt.grid(True)

plt.tight_layout()
plt.show()