def filtraMultiplos(lista_entrada,num):
    """..."""
    contador = 0
    lista_multiplos = []
    
    while contador<len(lista_entrada):
        if lista_entrada[contador]%num==0:
            list.append(lista_multiplos,lista_entrada[contador])
        contador = contador+1
    return lista_multiplos