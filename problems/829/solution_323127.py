def soma_h(n):
    
    '''Função que dado um valor n,
    retorna o resultado de H
    
    :param n: int
    :return:float'''
    
    
    soma=0
    
    
    for x in range (1, n+1):
        soma=soma+1/x
    return round(soma,2)