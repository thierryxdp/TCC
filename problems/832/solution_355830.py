def eh_quadrada(matriz):
    
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            
            linha=len(matriz[i]) 
            if linha==0:
                return True
            elif len(matriz)!=len(matriz[i]):
                return False
            else:
                return True