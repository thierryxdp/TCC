def media_matriz(matriz):
    soma = 0  
    contador = 0  
    
    for elemento in matriz:  
        for i in elemento:  
            soma += i  
            contador += 1  
    media = soma/contador  
    
    return round(media, 2)