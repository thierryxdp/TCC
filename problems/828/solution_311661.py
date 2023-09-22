def primo(numero):
    """ função que dado um número inteiro positivo, retorna se esse número é primo ou não;
    int -> int"""
    acumulador = 0
    for indice in range(1,numero):
        if numero % indice == 0:
            acumulador = acumulador + 1
    if acumulador <= 2:
        return 'True'
    else:
        return 'False'