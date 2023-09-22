def fatorial(numero):
    """funcao que calcula o fatorial de um numero;int->int"""
    num=list(range(numero,0,-1))
    i=0
    fat=1
    while i<len(num):
        fat=fat*num[i]
        i=i+1
    return fat