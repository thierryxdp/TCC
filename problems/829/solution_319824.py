def soma_h(numero):
    ''' função que calcula e retorna o valor H com N termos onde N é inteiro e dado com entrada.
    Entrada: int;
    Saída: int'''
    acumulador = 0
    divisor = 0
    for i in range(numero + 1):
        divisor = divisor + i
        acumulador = acumulador + 1
    return acumulador/divisor