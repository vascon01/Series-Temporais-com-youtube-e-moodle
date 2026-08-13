from banco import *

def main():
    operacoes_data()
    pass


def operacoes_data():
    dia=pd.Timestamp("2004-12-07") #!Especificar o dia da semana
    m(f"Dia da semana: {dia.day_name()}")
    
    dia2=dia+pd.Timedelta("3 day") #!Adicionar mais dias 
    m(dia2.day_name())
    
    dias_uteis=dia2+pd.offsets.BDay() #! Pula pro proximo dia util
    m(dias_uteis)
    
    frequencia_de_series_temporais()
    


def frequencia_de_series_temporais():
    periodo=pd.date_range("2019",freq="H",periods=25) #!Criamos um periodo de tempo de um dia em relação a hora
    ts=pd.Series(range(len(periodo)),index=periodo) #Basicamanete cria uma serie 
    
    #! Quero especificar uma frequencia de um periodo de 2 em 2 horas 
    m(ts.resample('2H').mean())
    


if __name__ == "__main__":
    main()