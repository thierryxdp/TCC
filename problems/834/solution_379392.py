def media_matriz(matriz):
    '''Dada uma matriz de inteiros não vazia, retorna a média de todos os numeros da matriz
    com a precisao de duas casas decimais; list[int] -> float'''
    i=0
    n=[]
    for linha in matriz:
        j=0
        for col in matriz[i]:
            n.append(matriz[i][j])
            j+=1
        i+=1
    return round((sum(n)/len(n)),2)