def media_matriz(matriz):
    """Funcao que retorna a media de todos os numeros de uma matriz.
    list(list) - > float"""
    soma = [] 
    qtd= 0
    for linha in matriz:
        for aij in linha:
            list.append(soma,aij)
            qtd += 1
    soma = sum(soma)
    return round((soma/qtd),2)