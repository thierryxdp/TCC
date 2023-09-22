def primo(numero:int)->bool:
    """ A função recebe um número inteiro positivo e verifica se ele é primo ou não. Caso seja primo retorna um booleano, True. Caso não retorna False"""
    eh_primo = ''
    while numero < len(numero):
        if numero[indice] % 2 != 0:
            eh_primo += 'True'
        else:
            eh_primo += 'False'
    return eh_primo