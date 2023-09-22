def faltante(l):
    '''Recebe uma lista 'l' de tamanho 'n' - 1 de números inteiros de
    1 a 'n'(não repetidos) e descobre qual número entre 1 e 'n' não está
    na lista 'l'.
    Retorna o número inteiro que pertence ao intervalo [1, n]
    mas não esstá na lista 'l'.
    
    list -> int'''
    
    n = len(l) + 1
    listaCompleta = range(1, n+1)
    indice = 0

    while indice < len(listaCompleta):
        if  listaCompleta[indice] not in l:
            return listaCompleta[indice]
        indice = indice + 1