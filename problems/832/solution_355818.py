def eh_quadrada(matriz):
     
         if [] in matriz:
                return True
    
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            
            if [] in matriz:
                return True
           
            elif len(matriz)==len(matriz[i]):
                return True
            else:
                return False