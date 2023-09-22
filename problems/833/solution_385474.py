def conta_numero(numero,matriz):
    """dado um número inteiro e uma matriz de inteiros de tamanho
 qualquer, conta e retorna quantas vezes aquele número aparece na matriz.
list->int"""
    tudo=0
    for i in matriz:
        for a in matriz:
            if numero==a:
                tudo=tudo+1
    return total