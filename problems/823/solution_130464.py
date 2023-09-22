def faltante(lista):
    """"""
    i = 1
    final = 0
    
    while i <= len(lista):
        if i not in lista:
            final = final + i
        i = lista[i-1]+1
    if final == 0:
        final += len(lista)+1
    return final