def qtd_divisores(n):
    '''Dado um número n qualquer, conta quantos 
    divisores um número tem
    int -> int'''
    qd = 0
    for i in range(1,n+1):
        if n%i==0:
            qd += 1
    return qd