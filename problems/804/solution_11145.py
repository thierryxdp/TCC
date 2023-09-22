def filtra_pares(tup):
    """Recebe uma tupla com 4 elementos inteiros como parâmetro e retorna uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam> Tupla--> Tupla"""
    
    if (tup[0]%2==0) or(tup[1]%2==0) or (tup[2]%2==0) or(tup[3]%2==0):
        return tup[0]+tup[1]+tup[2]+(tup[3]