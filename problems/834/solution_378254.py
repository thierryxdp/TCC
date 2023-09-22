def media_matriz(matriz):
    """ Dada uma matriz de inteiros nã vazia, retorna a média se todods os números da matriz;
    list->int """
    lista=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            lista.append(matriz[i][j])
    return round(sum(lista)/len(lista),2)