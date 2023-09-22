import itertools
def intercala(lista1,lista2):
    """intercala duas listas"""
res = list(itertools.chain(*zip(lista1, lista2))) 
return res