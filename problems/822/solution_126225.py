def repetidos(lista):
    '''
    Dado uma lista de números determina a quantidade de vezes que um
    elemento foi igual ao elemento anterior.

    Uso:
    repetidos(lista_num)

    Entrada:
    - lista (list): Lista original

    Saída:
    - Retorna o número de vezes que um elemento foi igual ao elemento anterior. (int)
    '''

    i = 1
    repeticoes = 0
    while i < len(lista):
        if lista[i] == lista[i - 1]:
            repeticoes = repeticoes + 1
        i = i + 1
    return repeticoes