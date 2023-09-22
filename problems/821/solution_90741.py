def fatorial(num):
    '''função para calcular o fatorial 
       de um determinado numero
    '''
    num=num if num>1 else 1
    indice=1
    for contador in range(1, num + 1):
        indice= indice*contador
    return indice