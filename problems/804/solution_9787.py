def filtra_pares(quatro_elementos):
    '''Função que recebe quatro elementos inteiros em uma
    tupla, verifica quais destes são pares e adiciona os 
    tais em uma nova tupla
    (int, int, int, int) -> tuple'''
    tupla = ()
    for n in quatro_elementos:
        if n%2 == 0:
            tupla + (n,)
            return tupla