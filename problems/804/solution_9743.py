def filtra_pares(quatro_elementos):
    '''Função que recebe quatro elementos inteiros em uma
    tupla, verifica quais deles são pares e retorna estes
    em uma nova tupla
    (int, int, int, int) -> (???)'''
    return (n for n in quatro_elementos if n%2 == 0)