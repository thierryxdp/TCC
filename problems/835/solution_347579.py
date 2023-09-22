def melhor_volta(matriz):
    j=0
    i=0
    tempo=0
    corredor=0
    lista_tempos=[]
    for j in range(len(matriz)):
    	for i in range(len(matriz[j])):
            if min(matriz[j])==i:
                
                lista_tempos=lista_tempos+[i]
    return list.index(lista_tempos,min(lista_tempos)),min(lista_tempos)