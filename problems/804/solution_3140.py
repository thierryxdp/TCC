def filtra_pares(t):
    """Função que retorna uma nova tupla contendo apenas os elementos pares da tupla de entrada,
    na mesma ordem em que se encontravam. tuple(int,int,int,int)->tuple"""
    novatupla= ()
    
    if t[0] % 2 == 0:
        novatupla = novatupla + (t[0],)
    
    if t[1] % 2 == 0:
        novatupla = novatupla + (t[1],)
    
    if t[2] % 2 == 0:
        novatupla = novatupla + (t[2],)
    
    if t[3] % 2 == 0:
        novatupla = novatupla + (t[3],)
        return novatupla