def filtraMultiplos(lista,n):
    """..."""
    contador = 0
    lista_ac = []
    
    while contador<len(lista):
        if lista[contador]%n==0:
            list.append(lista_ac,lista[contador])
        contador = contador+1
    return lista_ac