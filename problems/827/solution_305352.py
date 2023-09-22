def qtd_divisores(n):
    '''Recebe um numero e retorna a sua quantidade de divisores;
    int -> int'''
    lista=[]
    x=list(range(1,n+1))
    for i in x:
        if n%x[i]==0:
            lista=lista+[i]
    return len(lista)