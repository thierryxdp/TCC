def media_matriz(matriz):
    '''retorna a média de todos os números da matriz; 
    entrada->matriz; list(mat)->float'''
    quant_lin= len(matriz)
    quant_col=len(matriz[0])
    quant_elem = quant_lin * quant_col
    lista_elem= []
    for linha in matriz:
        for elem in linha:
            list.append(lista_elem,elem)
    media= (sum(lista_elem,0))/quant_elem
    media_final= round(media,2)
    return media_final