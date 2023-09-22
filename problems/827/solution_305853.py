def qtd_divisores(n):
    ''' Função que informa a qantidade de divisores de um numero n.
    int -> int'''
    d=0
    for i in range(1,(n)):
        if(n%i == 0):
            d=d+1
        return d