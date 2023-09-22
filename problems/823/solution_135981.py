def faltante (lista):
    """ dada uma lista de 1 a n sem repeticao, retorna o inteiro faltante na lista;
    list->int"""
    aux=[]
    for falta in range(len(lista)-1):
        if lista[falta+1] != lista[falta]+1:
            aux.append(lista[falta]+1)
    return aux