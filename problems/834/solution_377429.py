def media_matriz(matriz):
    media=0
    for i in matriz:
        
        for k in i:
            media+=k
            
        return media/(len(matriz)*len(matriz[0]))