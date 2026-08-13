from banco import *

def main():
    #Serve pra suavizar as curvas tirar a sujeira
    #! df.diet.rolling(12).mean().plot(figsize=(15,6))
    
    #Sazonalidade pra ver a ciclicadade
    #!df.diet.diff().plot()
    
    filtro=(df.index.year>=2005) & (df.index.year<=2007)
    #! df[filtro].diet.diff().plot(figsize=(15,6))
    
    df.diet.diff().groupby(df.index.month).mean().plot(kind='bar',figsize=(15,6))
    
    
    plt.show()

if __name__ == "__main__":
    main()