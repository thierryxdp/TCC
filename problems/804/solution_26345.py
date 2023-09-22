def filtra_pares(t):
    """recebe uma tupla contendo 4 numeros inteiros. retorna uma tupla contendo os elementos que sejam par. tuple --> tuple."""
    contador = 0
    tupla = ()
    while contador < len(t):
        if t[contador]%2 == 0:
            tupla += t[contador],
        contador +=1
    return tupla