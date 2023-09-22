def conta_numero(numero,matriz):
    '''retorna quantas vezes o número aparece na matriz de números inteiros;
    int, list(list) -> int'''
    ocorrencias = 0
    for i in matriz:
        qtd = list.count(i,numero)
        ocorrencias += qtd
    return ocorrencias