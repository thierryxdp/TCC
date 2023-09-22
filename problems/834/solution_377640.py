def media_matriz(matriz):
    """
    Media de todos os numeros da matriz.

Parametros:
	matriz:list,
    matriz não vazia.
    
Saida:
	float,
    media da matriz com duas casas decimais.
"""
    media=[]
    sequencia=0
    contagem=0
    
    for sequencia in range(len(matriz)):
        
        for contagem in range(len(matriz[sequencia])):
        	media.append(matriz[sequencia][contagem])
            
    return round(sum(media)/len(media),2)