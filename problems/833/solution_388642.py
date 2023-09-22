def conta_numero(numero,matriz):
    """Função que dado um número inteiro e uma matriz de inteiros, retorna
quantas vezes o número aparece na matriz; int,list->int"""
    vezes=0
    for elemento in matriz:
        for n in elemento:
            if n==numero:
                vezes+=1
    return vezes