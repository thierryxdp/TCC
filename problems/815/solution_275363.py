def insere(lista_numero,n):
    """
"""
    x = lista_numero

    for i, n in range(x):
        if x[i]<=n<=x[i+1]:
            x.insert(x[1],n)
    return x