def soma_h(n):
    """ Somatório de 1 sobre um dado número inteiro n;
    int -> float """
    ls=[]
    for i in range(1,n+1):
        if i != n+1:
            round(i,2)
            ls.append(1/i)
    return sum(ls)