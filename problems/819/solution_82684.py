def filtraMultiplos(numeros,n):
    """dada uma lista numeros de entrada, e um numero inteiro n
    retorna uma nova lista, com os numeros da lista numeros multiplos de n
    list, int --> list"""
    contador=0
    lista_multiplos=[]
    while contador < len(numeros):
        if numeros[contador]%n==0:
            lista_multiplos.append(numeros[contador])
        contador=contador+1
    return lista_multiplos