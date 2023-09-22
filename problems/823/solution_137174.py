def faltante(lista):
    """dado uma lista com numeros inteiros retorna o numero faltante"""
    i = 0
    lista.sort()
    while i < len(lista):
        if lista[i]-1 not in lista and lista [i]-1!=0:
            return lista[i]-1
        
        i+=1
    return lista[-1]+1