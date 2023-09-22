def uppCons(lista):
    """
    """
    lista_nova = lista
    
    for i in lista:
        if i not in  "aeiou":
            lista_nova = lista.upper()
        return lista_nova