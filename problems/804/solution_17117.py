def filtra_pares(a,b,c,d):
    '''função que recebe uma tupla (ent int) com 4 elementos inteiros como parâmetro e retorna uma nova tupla contendo apenas os pares (saida int)'''
    
    filtrototal = (a,b,c,d)
    posfiltro = ()
    if a%2==0:
        return posfiltro + a
    if b%2==0:
        return posfiltro + b
    if c%2==0:
        return posfiltro + c
    if d%2==0:
        return posfiltro + d