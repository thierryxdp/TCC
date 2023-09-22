def filtra_pares(a):
    "Filtre os pares da tupla inserida; tupla->tupla"
    j=([i for i in a if i%2==0])
    return tuple(j)