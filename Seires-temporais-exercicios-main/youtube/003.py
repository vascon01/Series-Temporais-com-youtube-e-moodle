import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# Carrega os dados
df = pd.read_csv("shampoo.csv")


# Transforma Month em data
df.Month = pd.to_datetime(df.Month)


# Define Month como índice
df.set_index("Month", inplace=True)


# Cria X1 = Sales do período anterior
df["X1"] = df.Sales.shift(1)


# Modelo Naive
def modelo_naive():
    # A previsão é o valor anterior de Sales
    df["Naive"] = df["X1"]

    # Calcula o erro quadrático médio (MSE)
    erros = ((df.Sales - df.Naive) ** 2).mean()

    return erros


# Modelo Auto-Regressivo
def modelo_auto_regressivo():

    # Remove a primeira linha, pois X1 é NaN
    dados = df.dropna()

    # Variável independente
    X = dados["X1"].values

    # Variável dependente
    y = dados["Sales"].values

    # Cria e treina o modelo
    reg = LinearRegression().fit(X.reshape(-1, 1), y)

    # Faz as previsões
    previsoes = reg.predict(X.reshape(-1, 1))

    # Calcula o erro quadrático médio
    erro = ((y - previsoes) ** 2).mean()

    
    plt.scatter(X,y)
    plt.plot(X,reg.predict(X.reshape(-1,1)),color="red")
    plt.xlabel("x1")
    plt.show()


    return erro


# Executa os modelos
print(f"MSE Naive: {modelo_naive()}")
print(f"MSE Auto-Regressivo: {modelo_auto_regressivo()}")

# Mostra os dados
print(df)