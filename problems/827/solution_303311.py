def qtd_divisores(n):
    '''Essa função diz quantos divisores o numero 'n' tem. int -> int'''
    a=0
    i=1
    while i <= n:
        if n%i == 0:
            a+=1
        i+=1
    return a