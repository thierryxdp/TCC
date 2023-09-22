def eh_quadrada(matriz):
    
    vazio=[]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            
            if len(matriz)==1 and len(matriz[i])==0:
                return True
           
            elif len(matriz)==len(matriz[i]):
                return True
            else:
                return False