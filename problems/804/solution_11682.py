def filtra_pares(quatro_elementos):
    '''Função que recebe quatro elementos inteiros em uma
    tupla, verificas quais desses são pares e os retorna
    em uma nova tupla
    (int, int, int, int) -> (tuple)'''
    tupla_vazia = ()
    for n in quatro_elementos:
        if n%2 == 0:
            tupla_vazia + (n,)
    return tupla_vazia