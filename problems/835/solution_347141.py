def melhor_volta(matriz):
    """Funcao que ira retornar quem foi a melhor volta da prova, com qual tempo e em que volta ; lista->tupla"""
    lista = []
    for segundo in matriz:
        lista = lista + [min(segundo)]
    num = list.index(lista,min(lista))
    volta = list.index(matriz[num],min(lista))
    return num+1,matriz[num][volta],volta+1