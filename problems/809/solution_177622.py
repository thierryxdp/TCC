def intercala(lista1, lista2):
    """Intercala duas listas de até 3 elementos no modelo a,b,a,b,a,b"""
    l1=lista1
    l2=lista2
    l3= l1[:1]+l2[:1]+l1[1:2]+l2[1:2]+l1[2:]+l2[2:]
    return l3