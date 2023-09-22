def media_matriz(X):
    """Função que dada uma matriz de inteiros não vazia, retorna a média dos números da mesma."""
    lista=[]
    for i in X:
        for j in i:
            lista.append(j)
    col=len(X[0])
    lin = len(X)
    relacao = lin * col
    return round(sum(lista)/relacao,2)