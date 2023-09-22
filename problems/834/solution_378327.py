def media(matriz):
    """retorna media dd todos os itens de uma matriz não vazia
    list(list) -> float"""
    med = 0
    for linha in matriz:
        for elemento in linha:
            med = med + elemento
        conta = med/(len(matriz)*len(matriz[0]))
    return round(conta,2)