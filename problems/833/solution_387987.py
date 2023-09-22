def conta_numero(num,matriz):
    '''dado um numero inteiro e uma matriz de numeros inteiros, conta e retorna quantas vezes aquele numero aparece na matriz'''
    qtd_vezes=0
    for lista in num:
        for elem in lista:
            if elem == matriz:
                qtd_vezes += 1
    return qtd_vezes