def melhor_volta(matriz):

    '''
    Função que recebe uma matriz como parâmetro e retorna
    a média dos termos da mesma.

    none -> float
    '''

    lin = len(matriz)
    col = len(matriz[0])
    t_linha = []
    t_coluna = []
    
    for i in range(lin):
        lista1 = []
        for j in range(col):
            lista1.append(matriz[i][j])
        t_linha.append(lista1)

    for j in range(col):
        lista2 = []
        for i in range(lin):
            lista2.append(matriz[i][j])
        t_coluna.append(lista2)
    
    lista_menor = []
    tam = len(t_linha)
    for x in range(tam):
        mini = min(t_linha[x])
        lista_menor.append(mini)
    menor = (min(lista_menor))

    for i in range(lin):
        if matriz[i] in t_linha:
           linha = i
           
    coluna_m = matriz[linha-1][0:]
    
    for j in range(col):
        if coluna_m[j] == menor:
           coluna = j+1
    
    return (linha, menor, coluna)