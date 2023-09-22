def soma_h(n):
    """ Somatório de 1 sobre um dado número inteiro n;
    int -> float """
    ls=[]
    z=1
    for i in range(1,n+1):
        if i != n+1:
            ls.append(1/i)
        z+=1
    return round(sum(ls),2)