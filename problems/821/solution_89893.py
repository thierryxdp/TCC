def fatorial(numero):
    '''Função que calcula o fatorial de um número
    valor de entrada: int
    valor de saída: int'''
    num=1
    while numero>0:
        num=num*numero
        numero=numero-1
    return num