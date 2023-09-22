def fatorial(n):
    ''' função que dado um número, calcule o fatorial deste número.
    Entrada: int;
    Saída: int'''
    calculadora = 1
    proximo = n
    while proximo > 1 :
        calculadora = calculadora*proximo
        proximo = proximo - 1
    return calculadora