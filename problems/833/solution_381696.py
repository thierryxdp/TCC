# Buscando na Matrz
def conta_numero(numero, matriz):
    '''Ao receber um número inteiro e uma matriz, a função retorna a
    quantidade de vezes que número aparece em matriz;
    INT, LIST -> INT'''
    conta = 0
    for i in matriz:
        for j in matriz[0]:
            if j == numero:
                conta += 1
    return conta