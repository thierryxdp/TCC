def soma_h(n):
    """essa função calcula o valor de H com N termos 
    com valor retornado em duas casas decimais;
    int->float"""
    h = 0
    
    for i in range(1,n+1):
        h += 1/i
    return round(h,2)