def media_matriz(matriz_int):
    '''
    funcao que retorna a media, com 2 casas deciamis, dos numeros de uma
    matriz de entrada nao vazia, contendo inteiros
    list->float 
    '''
    contador_lista=0
    for vetor_confere in range(len(matriz_int)):
        ultimo_elem_lista=matriz_int[vetor_confere]
        for num_contar in range(len(ultimo_elem_lista)):
            contador_lista=contador_lista+ultimo_elem_lista[num_contar]
    media_matrix=(contador_lista/(len(matriz_int)*len(matriz_int[0])))        
    return round(media_matrix,2)