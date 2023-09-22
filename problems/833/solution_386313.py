def conta_numero(numero,matriz):
    '''Dado um número inteiro e uma matriz de inteiros de tamanho
    qualquer, retorna quantas vezes aquele número aparece na matriz
    int,mat->int'''
    for lin in matriz:
        for elemento in lin:
            if elemento==numero:
                return True
    return False