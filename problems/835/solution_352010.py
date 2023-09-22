def melhor_volta(matriz):
    lista=[]
    for i in matriz:
        lista+=min(matriz[i][1:])
        
    tempo=min(lista)
    volta=lista.index(tempo)
    for i in lista:
        if tempo in lista:
            corredor= matriz[i][0]
           
    
    return (corredor, tempo, volta)