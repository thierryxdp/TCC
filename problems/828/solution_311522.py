def primo(numero):
    ''' função que dado um número inteiro positivo, verifique se este número é primo ou não.
    entrada: int;
    saída: str'''
    acumulador = 0
    for indice in range(1,numero + 1):
        if numero % indice == 0:
            acumulador = acumulador + 1
    if acumulador <= 2:
        return 'True'
    else:
        return 'False'