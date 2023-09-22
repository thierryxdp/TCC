def intercala(lista1,lista2):
    """intercala duas listas"""
    res = lista1 + lista2 
res[::2] = lista1 
res[1::2] = lista2