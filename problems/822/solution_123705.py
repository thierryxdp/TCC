def repetidos(lista):
    """funcao que retorna a quantidade de elemntos repetidos em uma lista;list->int"""
    i=0
    rep=0
    while i<len(lista):
        if lista[i]==lista[(i-1)]:
            rep=rep+1
            i=i+1
    return rep