def fatorial(numero):
    '''função para calcular o fatorial de um determinado 
    	numero.int-->int'''
    numero=numero if numero>1 else 1
    indice=1
    while numero in range(1, numero + 1):
        indice= indice*numero
    return indice