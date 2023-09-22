def soma_h(n):
    '''
        dado um n inteiro retorn a soma de n termos de 1/1 até 1/n
        int -> float
    '''
    h=0
    for n in range(1,n+1):
        h=h+(1/n)
    return round(h,2)