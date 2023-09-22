def soma_h(n):
    """coment"""
    soma=0
    for x in range(1,n+1):
        x=1/x
        soma+=x
    return round(soma,2)