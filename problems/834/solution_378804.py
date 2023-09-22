def media_matriz(m):
    """Função que, dada uma matriz de inteiros não vazia, retorna a média de todos os números da matriz com exatamente duas casas decimais de precisão"""
    n=0
    l=[]
    for i in range(len(m)):
        for j in range (len(m[0])):
            	n=n+int(m[i][j])
                l=l+[m[i][j]]
    return round((n/len(l)),2)