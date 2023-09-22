def busca(elemento,matriz):
    """Determina o menor tempo dentre vários corredores em uma corrida"""
    listafinal = []
    indexcorredor = []
    indexvolta = []
    m = len(matriz)
    for i in range(len(matriz)):
        if elemento in matriz[i]:
            lista = del(matriz[i],[2])
            list.append(listafinal,lista)
    return listafinal