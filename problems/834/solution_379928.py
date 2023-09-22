def media_matriz(m):
    """Dada uma matriz de inteirod não vazia, retorna a média de todos
    os números da matriz"""
    media = []
    for linha in m:
        media += sum(linha)
    return round(media/(len(m)*len(m[0]))),2)