def melhor_volta(matriz):
    lista=[]
    volta=[]
    linha=len(matriz)
    coluna=len(matriz[0])
    for i in range(linha):
    	list.append(lista,min(matriz[i]))
        list.append(volta,list.index(matriz[i],min(matriz[i]))+1)
    menor_tempo=min(lista)
    Corredor_menor_tempo=list.index(lista,menor_tempo)+1
    qual_volta=min(volta)
    return (Corredor_menor_tempo, menor_tempo, qual_volta)