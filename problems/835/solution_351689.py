def melhor_volta(matriz):
    ''''''
    tupla=[]
    for lista in matriz:
        menores=min(lista)
        tupla=tupla+[menores]
        tempo=min(tupla)
        
    corredor=list.index(tupla,tempo)
    volta=list.index(matriz[corredor],tempo)
    
    return tempo, corredor+1, volta+1