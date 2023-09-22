def conta_numero(numero,matriz):
    """Dado um númeor inteiro e uma matriz de inteiros de tamanho qualquer,
    conta e retorna quantas vezes aquele número aparece na matriz"""
    for numero in matriz:
        return list.count(matriz,numero)