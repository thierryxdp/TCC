def media_matriz(mat):
    """dada uma matriz de inteiros nao vazia, retorna a 
    media de todos os numeros dessa
    list(of lists)->float"""
    final=[]
    for linha in mat:
        x=sum(linha)
        y=len(linha)
        final.append(x/y)
    return round(sum(final),2)