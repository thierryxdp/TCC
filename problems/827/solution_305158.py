def qtd_divisores(n):
    '''Recebe um numero e retorna a sua quantidade de divisores;
    int -> int'''
    lista=[]
    for divisor in list(range(n+1)):
        if n%divisor=0:
            lista= lista+[divisor]
    return len(lista)