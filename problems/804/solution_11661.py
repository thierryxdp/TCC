def filtra_pares(quatro_elementos):
    '''Função que recebe quatro elementos inteiros em uma
    tupla, verifica quais desses são pares e retorna eles
    em uma nova tupla
    (int, int, int, int) -> (tuple)'''
    if quatro_elementos%2 == 0:
        return quatro_elementos