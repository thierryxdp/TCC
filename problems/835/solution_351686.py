def melhor_volta(matriz):
    ''''''
    tupla=[]
    for lista in matriz:
        menores=min(lista)
        tupla=tupla+[menores]
        tempo=min(tupla)
        
    corredor=list.index(tupla,tempo)
    
    volta=list.index(tupla,matriz[corredor])
    
    return volta+1