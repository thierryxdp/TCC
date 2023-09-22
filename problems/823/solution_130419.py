def faltantes(L):
    if L:                   
        elemento = L[0]               
        posicao = 1                   
        while posicao < len(L):       
          
            if (elemento + 1) < L[posicao]: 
                elemento += 1        
                yield elemento        
            else:                     
                elemento = L[posicao] 
                posicao += 1