def melhor_volta(matriz):
    contadorvolta=[]
    ndevolta=0
    contadorcorredor=[]
    contadortempo=[]
    for volta in matriz:
        contadorvolta.append(volta.index(min(volta)))
        contadortempo.append(min(volta))
		 
    return (contadortempo.index(min(contadortempo)), min(contadortempo), int(contadorvolta[contadortempo.index(min(contadortempo))])+1)