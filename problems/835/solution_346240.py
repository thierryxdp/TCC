def melhor_volta(matriz):
    """Retorna qual corredor na pista de Kart foi a melhor volta da prova com qual tempo e em que volta.
    Parametros:
    Entrada:list
    Saida:tupla"""
    
    lista=[]
    linha=len(matriz)
    coluna=len(matriz[0])
    for i in range(linha):
    	list.append(lista,min(matriz[i]))
    menor_tempo=min(lista)
    Corredor_menor_tempo=list.index(lista,menor_tempo)+1
    qual_volta=list.index(matriz[Corredor_menor_tempo-1],menor_tempo)+1
    return (Corredor_menor_tempo, menor_tempo, qual_volta)