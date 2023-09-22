def soma_h(x):
    """retorna a soma de números 1+1/2+1/3+...+1/n em duas casas decimais
    int->float"""
    s=0
    for n in range(x+1):
        if n==0:
            s=0
        else:
            s+=1/n
    return round(s,2)