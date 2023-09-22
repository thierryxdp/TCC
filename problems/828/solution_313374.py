def primo(n):
    
    contador = 0
    for numero in range(2, n):
        if numero % n == 0:
            contador += 1
        if not numero % n == 0:
       		contador += 0
            
            if contador > 2:
                return False
            else:
                return True 
            
            
            
            ifcontador > 2:
                return False 
            
            for contador <= 2:
                return True