def soma_h (N: int)->float:
    '''Retorna o valor da soma 1+ 1/2 + 1/3 + 1/4 +...+ 1/N , dado 
    o valor de N''' 
    numero = 1
    for elem in range(N+1):
        if elem != 0:
            numero= numero + elem**(-1)
    return numero