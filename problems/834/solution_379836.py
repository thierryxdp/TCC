def media_matriz(matriz):
    '''Recebe uma matriz inteira e não vazia e retorna
    a média de todos os números dessa matriz.'''
    #total da soma de todos os números da matriz
    total_numeros = 0
    #tamanho de cada linha
    total_tamanho = 0
    if matriz!=[]:
        #Percorre cada linha da matriz
        for i in matriz:
            #Soma o tamanho da linha
            total_tamanho+=len(i)  
            #percorre cada número da linha
            for n in i:
                #Soma pro total de números
                total_numeros +=n         
    return round(total_numeros/total_tamanho,2)