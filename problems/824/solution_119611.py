def uppCons(lista):
    """
    """
    lista_nova = lista
    
    for i in lista:
        if i in "aeiou":
            lista_nova.replace(lista,lista_nova)
            return lista_nova