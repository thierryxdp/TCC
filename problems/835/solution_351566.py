def melhor_volta(matriz):
    ''''''
    tupla=[]

    for lista in matriz:
        menores=min(lista)
        tupla=tupla+[menores]
        tempo=min(tupla)
        
    
    corredores=list.index(menores,tempo)
 
    return corredores