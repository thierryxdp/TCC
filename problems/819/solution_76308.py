def filtraMultiplos(lista,n):
    """..."""
    contador = 0
    lista_multiplos = []
    
    while contador<len(lista):
        if lista[contador]%n==0:
            list.append(lista_multiplos,lista[contador])
        contador = contador+1
    return lista_multiplos