def media_matriz(matriz):
    """Dada uma matriz de inteiros (não vazia), retorna
a média dos números que estão na matriz, com precisão de duas
casas decimais.
assinatura:
mat --> float
casos de teste:
media_matriz([[1, 1, 1]]) == 1.0
media_matriz([[10], [10]]) == 10.0
media_matriz([[200], [100]]) == 150.0
media_matriz([[2, 4, 6], [2, 4, 6]]) == 4.0
"""
    ls = []
    for n in matriz:
        for x in n:
            list.append(ls, x)
    soma = sum(ls)/len(ls)
    return round(soma,2)