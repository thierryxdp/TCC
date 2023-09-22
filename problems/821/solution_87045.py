def fatorial(numero):
    '''função para calcular o fatorial de um determinado numero'''
    numero=numero if numero>1 else 1
    indice=1
    for contador in range(1, numero + 1):
        indice= indice*contador
    return indice