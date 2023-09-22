import itertools
def intercala(lista1,lista2):
    """intercala duas listas"""
    lista1 = [] 
    lista2 = [] 
res = list(itertools.chain(*zip(lista1, lista2))) 
print ("The interleaved list is : " + str(res))