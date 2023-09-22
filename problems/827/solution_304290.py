def qtd_divisores(num):
    
    resultado = 0    
    for contador in range(1, num+1):
        if num % contador == 0:
            resultado += 1
        
        else:
            pass
       
    return resultado