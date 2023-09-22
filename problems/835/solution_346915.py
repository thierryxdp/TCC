def melhor_volta(matriz):
    """Função que retorna de quem foi a melhor volta da prova com qual tempo e em que volta. List--> Str"""
    lista = []
    for segundo in matriz:
        lista = lista + [min(segundo)]
    num = list.index(lista,min(lista))
    volta = list.index(matriz[num],min(lista))
    return num+1,matriz[num][volta],volta+1