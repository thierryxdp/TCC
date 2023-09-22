def melhor_volta(matriz):
    contadorvolta=[]
    ndevolta=0
    contadorcorredor=[]
    contadortempo=[]
    for volta in matriz:
        contadorcorredor.append(volta.index(min(volta)))
        contadortempo.append(min(volta))
    return (, min(contadortempo), int(contadorcorredor[contadortempo.index(min(contadortempo))])+1)