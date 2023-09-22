def melhor_volta(matriz):
    """recebe uma matriz com o tempo de volta de dviersos corredores em diversas voltas e retorna uma tupla com o o número do corredor com a volta mais rápida, o menor tempo de volta e o número da volta de certo jogador com o melhor tempo. LIST->TUPLE.""" 
    contadorvolta=[]
    ndevolta=0
    contadorcorredor=[]
    contadortempo=[]
    for volta in matriz:
        contadorvolta.append(volta.index(min(volta)))
        contadortempo.append(min(volta))
    return (contadortempo.index(min(contadortempo))+1, min(contadortempo), int(contadorvolta[contadortempo.index(min(contadortempo))])+1)