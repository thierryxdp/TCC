def media_matriz(matriz):
    '''Retorna a média de todos os números da matriz com duas casas decimais de precisão
    entrada: list
    saída: float
    '''
    somasdascolunas=[]
    for coluna in matriz:
        somanacoluna= sum(coluna)
        list.append(somasdascolunas,somanacoluna)
    mediatotal= sum(somasdascolunas)/(len(matriz)*len(matriz[0])
    mediaarredondada= round(mediatotal,2)
    return mediaarredondada