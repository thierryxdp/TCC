def media_matriz(matriz):
    '''
    Funçao que dada uma matriz de inteiros não vazia, retorna a media de todos os 
    numeros da matriz(com exatamente duas casas decimais de precisao)
    list(list) -> int
    '''
    elem = []
    media = 0
    qtd_elem = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            list.append(elem,matriz[i][j])
        qtd_elem = qtd_elem + len(matriz[i])
    media = sum(elem)       
    return round((media/i),2)