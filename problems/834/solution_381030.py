def media_matriz (matriz):
    """Retorna a média da matriz somando seus elementos (números inteiros) e dividindo pela quantidade de elementos. matriz -> float"""
    soma=0
    quantidade = 0
    for lista in matriz:
        for elemento in lista:
            soma += elemento
            quantidade += 1
    return round(soma/quantidade,2)