def media_matriz(matriz):
    '''dada uma matriz nao vazia, retorna a media de todos os numeros.
       list --> float'''
    qntd = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            list.append(qntd,matriz[i][j])
            
    denominador = len(matriz)*len(matriz[0])
    return round((sum(qntd)/denominador),2)