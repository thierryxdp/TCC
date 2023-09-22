def melhor_volta(matriz):
    '''funcao que retorna qual dos 6 corredores deu a melhor volta,
    e qual foi o melhor tempo dado por esse corredor e em qual das 10 
    voltas ele alcancou esse tempo
    list->tuple'''
    lista=[]
    indices=[]
    for i in range(len(matriz)):
            tempo=min(matriz[i])
            list.append(lista,tempo)
            indice=list.index(matriz[i],tempo)
            list.append(indices,indice)
            
    melhor_volta=min(lista)
    tempo_volta=list.index(lista,melhor_volta)
    posicao_volta=indices[tempo_volta]
    resultado=(tempo_volta+1,melhor_volta,posicao_volta+1)
    
    return resultado