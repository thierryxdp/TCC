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
        list.append(lista_tempo,min(corredor))
        #contador de voltas
        contador = 0
        for volta in corredor:
            if volta != min (corredor):
                contador +=1
            else:
                list.append(lista_volta,contador+1)
    
    
    menor_tempo = min(lista_tempo)
    #numero
    cont1 = 0
    #jogador
    for tempo in lista_tempo:
        if tempo != menor_tempo:
            cont1+=1
        else:
            cont1 = cont1+1
            break
    num_volta = 0            
    for elemento in matriz[cont1 - 1] :
        if elemento != menor_tempo:
            num_volta += 1
        else:
            num_volta = num_volta
            break
        
    lista_retorno = [cont1,menor_tempo,num_volta+1]
    
    return tuple(lista_retorno)