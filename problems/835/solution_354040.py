def melhor_volta(matriz): 
    # 6 lin 10 col == len(matriz) = 6 , len(matriz[0]) = 10
    """
    Essa funcao ira retornar uma tupla contendo as inforcoes do melhor corredor
    list->tuple
    """
    
    
    #lista com melhores tempos de cada corredor a lista tera 10 elementos
    lista_tempo=[]
    #lista contendo qual foi a melhor volta de cada corredor
    lista_volta=[]
    
    # 6 corredores, 10 voltas cada
    for corredor in matriz:
        list.append(min(corredor),lista_tempo)
        #contador de voltas
        contador = 0
        for volta in corredor:
            if volta != min (corredor):
                contador +=1
            else:
                list.append(lista_volta,contador)
         
    #melhor corredor
    contador_2 = 0
    index = 0
    index_2 = 0
    menor = lista_tempo[9] 
    
    while index < len(lista_tempo):
        if lista_tempo[index] < menor:
            contador_2 = lista_tempo[index] + 1
            index_2 = index
        index += 1
            
    return tuple(contador_2,lista_tempo[index_2],lista_volta[index_2])