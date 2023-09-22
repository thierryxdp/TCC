def filtraMultiplos(lista,n):
    """função que retorna uma lista com o multiplos de um numero"""
    mult=[]
    i=0
    while i < len(lista):
        if lista[i]%n == 0:
            mult.insert(len(lista),lista[i])
        i = i + 1
    return mult