def acima_da_media(l):
    """Pegamos os elementos da lista e comparamos para ver se sao maiores
    que o numero dado, caso sim organizamos numa lista e colocamos em ordem crescente
    str,int-->str
    """
    n=sum(l)
    d=[]
    for numeros in l:
        if numeros>n:
            d+=[numeros]            
    i=sorted(d)
    return i