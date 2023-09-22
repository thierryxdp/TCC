def fatorial(numero):
    '''
    Dado um número, retorna seu fatorial.

    Uso:
    fatorial(numero)

    Entrada:
    - numero (int): Número inteiro

    Saída:
    - Retorna o fatorial de um dado número. (int)
    '''

    i = 0
    fat = 1
    numero2 = numero
    while i < numero:
        fat = fat * numero2
        numero2 = numero2 - 1
        i = i + 1
    return fat