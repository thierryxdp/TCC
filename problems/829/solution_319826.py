def soma_h(numero):
    ''' função que calcula e retorna o valor H com N termos onde N é inteiro e dado com entrada.
    Entrada: int;
    Saída: float'''
    divisor = 0
    acumulador = 0
    for i in range(numero + 1):
        divisor = divisor + i
        var1 = 1/divisor
        acumulador = acumulador + var1
    return acumulador