def soma_h(numero):
    ''' função que calcula e retorna o valor H com N termos onde N é inteiro e dado com entrada.
    Entrada: int;
    Saída: int'''
    acumulador = 0
    for i in range(numero + 1):
        x = 1/i
        acumulador = acumulador + x
    return acumulador