def soma_h(numero):
    ''' função que calcula e retorna o valor H com N termos onde N é inteiro e dado com entrada.
    Entrada: int;
    Saída: float'''
    acumulador = 0
    for i in range(1,numero + 1):
        var1 = 1/i
        acumulador = acumulador + var1
    return round(acumulador,2)