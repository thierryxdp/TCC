def fatorial(numero):
    '''funçao dado um numero calcula o seu fatorial
    int -> int'''
    contador = 1
    resultado = numero * contador
    while contador < numero:
        resultado *= contador
        contador += 1
    return resultado