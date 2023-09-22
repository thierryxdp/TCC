def qtd_divisores (numero):
    '''Dada a função, retorne quantos divisores o número tem;
       int -> int'''
    cont = 0
    for i in list(range(1, n+1)):
        if (n%i)==0:
            cont = cont+1
    return cont