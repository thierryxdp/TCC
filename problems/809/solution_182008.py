def intercala(lista1,lista2):
    """intercala duas listas"""
    lista1 = [1, 4, 5] 
    lista2 = [3, 8, 9] 
res = lista1 + lista2 
res[::2] = lista1 
res[1::2] = lista2