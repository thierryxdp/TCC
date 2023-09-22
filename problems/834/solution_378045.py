def media_matriz(M):
    '''Função que dada uma matriz de inteiros, retorna a média de todos eles.
list -> int'''
    Lista=[]
    Resol=0
    for i in range(len(M)):
        for j in range(len(M[0])):
            Lista.append(M[i][j])
    Resol = sum(Lista)*1/len(Lista)
    return round(Resol,2)