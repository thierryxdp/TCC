def conta_numero(numero,matriz):
    '''Retorna quantas vezes o número inteiro aparece na matriz de inteiros;
    int, list -> int'''
    qtd=0
    for linha in matriz:
        qtd=qtd+list.count(linha,numero)
    return qtd