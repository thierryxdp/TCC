def melhor_volta(matriz):
    
    tempo=0
    corredor=0
    lista_tempos=[]
    for corredor in range(len(matriz)):
    	for tempo in range(len(matriz[corredor])):
            if min(matriz[corredor])==tempo:
                
                lista_tempos=lista_tempos+[tempo]
    return list.index(lista_tempos,min(lista_tempos)),min(lista_tempos)