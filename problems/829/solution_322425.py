def soma_h(n):
    '''funcao que calcula o valor de 
    h com somente duas casas decimais,
    sendo h= 1 + 1/2 + 1/2 ... 1/n 
    e n um numeo inteiro 
    entrada: inteiro
    saida: float
    '''
    h= 0
    for divisor in range(1,n):
        h= h + 1/divisor
    return round(h, 2)