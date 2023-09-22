def fatorial(n):
    """Função que calcula o fatorial de um numero n"""
    """int->int"""
    x=[]
    d=0
    e=0
    i=0
    while i<n:
        list.append(x,n-i)
        if i==1:
            d=x[i-1]*x[i]
            e=d
        elif i>1:
            e=e*x[i]
        i=i+1
        elif n==1:
            return 0
    return e