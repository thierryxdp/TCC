def media_matriz(m):
    """Função que recebe uma matriz de inteiros não vazia
    e retorna a média de todos os números dessa matriz (com
    exatamente duas casas decimais de precisão).
    
    list -> float
    """
    
    elementos_matriz = []
    soma = 0
    for i in range(len(m)):
        for j in m[i]:
            list.append(elementos_matriz,m[i])
            soma = soma + j
    media = soma/len(elementos_matriz)
    return round(media,2)