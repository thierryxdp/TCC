def eh_quadrada(matriz: list) -> bool:
    """Identifica se uma matriz é quadrada"""
    lista = []
    for i in range(len(matriz)):
        list.append(lista,len(matriz[i]))
    if sum(lista)/len(lista) == len(matriz):
        return (True,lista,len(lista))
    else:
        return (False,lista,len(lista))