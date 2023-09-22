def qtd_divisores(n):
    """dado um numero como parametro conta quantos divisores o numero possui;
    int->int"""
    x=1
    aux=0
    while x<=n :
        if  n%x==0 :
            aux=aux+1
        x=x+1
    return aux