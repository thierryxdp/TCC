def filtra_pares(algorismo):
    '''calcule uma função que receba uma tupla com quatro elementos inteiros, e retorne uma nova tupla contendo apenas os elementos pares da tupla original. tupla-->tupla.''''
    pares = [elementos for elementos in algorismo if elemento%2 != 1]
    return (tuple (pares))