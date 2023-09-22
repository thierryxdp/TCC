def melhor_volta(matriz):
    ''''''
    tupla=[]
    
    for list in matriz:
        menores=min(lista)
        tupla=tupla+[menores]
        tempo=min(tupla)
        
    corredor=list.index(min(menores))
    
    return corredor