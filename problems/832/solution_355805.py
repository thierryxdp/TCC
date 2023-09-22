def eh_quadrada(matriz):
    
    vazio=[]
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            
            if i==0 and j==0:
                return True
           
            elif len(matriz)==len(matriz[i]):
                return True
            else:
                return False