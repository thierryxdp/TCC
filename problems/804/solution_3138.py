def filtra_pares(t0,t1,t2,t3):
    """Função que retorna uma nova tupla contendo apenas os elementos pares da tupla de entrada,
    na mesma ordem em que se encontravam. tuple(int,int,int,int)->tuple"""
    novatupla= ()
    
    if t0 % 2 == 0:
        novatupla = novatupla + (t0,)
    
    if t1 % 2 == 0:
        novatupla = novatupla + (t1,)
    
    if t2 % 2 == 0:
        novatupla = novatupla + (t2,)
    
    if t3 % 2 == 0:
        novatupla = novatupla + (t3,)
        
        
        return novatupla