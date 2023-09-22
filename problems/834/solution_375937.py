def media_matriz(matriz):
     
    elementos=[]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            list.append(elementos,matriz[i][j])
            
    soma=sum(elementos)
    
    return round(soma//len(elementos))