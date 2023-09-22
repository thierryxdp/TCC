def eh_quadrada(matriz):
    
    vazio=[]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            
            if matriz[i]==vazio:
                return True
           
            elif len(matriz)==len(matriz[i]):
                return True
            else:
                return False