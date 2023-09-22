def filtra_pares (T):
    """dada uma tupla com quatro números inteiros como parâmetros
    ,retorna uma nova tupla contendo apenas os elementos pares da tupla original
    na mesma ordem em que se encontravam 
    entrada: tuple [0,0,0,0]
    retorna: tuple"""
    a,b,c,d= T
    
    par_a= (a%2)==0
    par_b= (b%2)==0
    par_c= (c%2)==0
    par_d= (d%2)==0
    
    if par_a and par_b and par_c and par_d:
        return tuple(a,b,c,d)