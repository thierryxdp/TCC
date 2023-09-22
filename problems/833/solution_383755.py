def conta_numero(numero,matriz):
    '''Dado um numero e uma matriz de qualquer tamanho retorna
    quantas veses o numero aparece na matriz'''
    qtd = 0
    for linha in matriz:
        for n in linha:
            if numero == n:
                qtd = qtd + 1
    return qtd