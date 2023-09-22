def filtra_pares(a,b,c,d):
    """retorne uma tupla contendo somente os números pares da tupla de entrada"""
    lista1=[str(a),str(b),str(c),str(d)]
    lista2= sorted(filter(lambda x:x%2==0, lista1))
    return lista2