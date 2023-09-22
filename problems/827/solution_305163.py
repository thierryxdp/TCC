def qtd_divisores(n):
    '''Recebe um numero e retorna a sua quantidade de divisores;
    int -> int'''
    lista=[]
    for d in list(range(n+1)):
        if n%d=0:
            lista=lista+[d]
    return len(lista)