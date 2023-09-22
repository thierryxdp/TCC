def fatorial(número):
    ''' função que dado um número, calcule o fatorial deste número.
    Entrada: int;
    Saída: int'''
    calculadora = 1
    proximo = número
    while número > 1 :
        calculadora = calculadora*proximo
        proximo = proximo - 1
    return calculadora