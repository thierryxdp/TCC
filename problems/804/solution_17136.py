def filtra_pares(a=None, b=None, c=None, d=None)
    '''função que recebe uma tupla com 4 elementos inteiros como parâmetro e retorna uma nova tupla contendo apenas os elementos pares da tupla original(ent -> int  saida -> int) '''
    
    
    
    
    filtrototal = ()
    
    if d%2==0:
        filtrototal = filtrototal + d
    
    if c%2==0:
        filtrototal = filtrototal + c
    
    if b%2==0:
        filtrototal = filtrototal + b
    
    if a%2==0:
        filtrototal = filtrototal + a