def repetidos(listadenumeros):
    """Funcao que recebe como entrada uma lista de numeros e retorna o numero de vezes que um elementos da lista e igual ao elemento anterior. list=>int"""
    lista=0
    x=1
    while x <len(listadenumeros):
        if listadenumeros[x]==listadenumeros[x-1]:
            lista=lista+1
        x=x+1
    return lista