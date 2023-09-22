def media_matriz(m):
    """Função que recebe uma matriz de inteiros não vazia
    e retorna a média de todos os números dessa matriz (com
    exatamente duas casas decimais de precisão).
    
    list -> float
    """
    
    elementos_matriz = []
    for i in m:
        for j in m[i]:
            list.append(elementos_matriz,m[i])
    media = sum(elementos_matriz)/len(elementos_matriz)
    return round(media,2)