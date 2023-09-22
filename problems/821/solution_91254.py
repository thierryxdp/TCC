def fatorial(x):
    'Função que calcula o fatorial de um número.'
    'int->int'
    
    c=0
    f=0
    n=1
    a=1
    lista=[]
    while c!=x:
        lista=lista+[a]
        c=c+1
        a=a+1
    b=len(lista)
    while f!=b:
        n=n*lista[f]
        f=f+1
    return n