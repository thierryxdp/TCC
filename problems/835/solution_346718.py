def melhor_volta(matriz):
    """funcao que recebe uma matriz e retorna uma tupla de quem foi a melhor volta, com qual tempo e em que volta.
    list->tupla."""
    x=[]
    y=()
    for i in range(len(matriz)):
        x.append((matriz[i].index(min(matriz[i]))+1,min(matriz[i]),i+1)
        y.append(min(matriz[i]))
    melhor=y.index(min(y))
    return (x[melhor])