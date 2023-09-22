def melhor_volta(matriz):
    ''''''
    tupla=[]

    for lista in matriz:
        menores=min(lista)
        tupla=tupla+[menores]
        tempo=min(tupla)
        
    corredores=list.index(menores,1)
 
    return corredores