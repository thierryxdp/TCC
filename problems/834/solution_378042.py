def media_matriz(M):
    '''Função que dada uma matriz de inteiros, retorna a média de todos eles.
list -> int'''
    Lista=[]
    for i in range(len(M)):
        for j in range(len(M[0])):
        	Lista.append(M[i][j])
    return sum(L)*1.0/len(L)