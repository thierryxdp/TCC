def media_matriz(m):
    """Retorna a média (com 2 casas decimais) de todos os 
    números de uma matriz de inteiros não vazia dada como 
    entrada.
    lista(lista) -> float"""
    soma = 0
    qtd_elem = len(m)*len(m[0])
    for l in range(0, len(m)):
        for c in range(0, len(m[l])):
            soma += m[l][c]
    media = soma/qtd_elem
    return round(media,2)