def soma_h(n):
    """dado o numero de termos, retorna o valor de H
    int->int"""
    h=0
    for t in range (1,n+1):
        h+=1/t    
    return round(h,2)