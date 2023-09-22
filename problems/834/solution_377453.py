def media_matriz(mat):
    """Dada uma matriz nao vazia, retorna a media de seus numeros
    entrada:
    	mat -> list
    saida: float"""
    
    tot = 0
    for i in range(len(mat)):
        tot += sum(mat[i])
    
    media = tot/(len(mat)*len(mat[0]))
    return round(media, 2)