def media_matriz(matriz):
    '''Retorna a média de todos os números da matriz com duas casas decimais de precisão
    entrada: list
    saída: float
    '''
    # Definindo a soma de cada coluna
    somasdascolunas=[]
    for coluna in matriz:
        somanacoluna= sum(coluna)
        list.append(somasdascolunas,somanacoluna)
    # Definindo a média total e arredondando a partir da segunda casa decimal
    mediatotal= sum(somasdascolunas)/(len(matriz)*len(matriz[0]))
    mediaarredondada= round(mediatotal,2)
    return mediaarredondada