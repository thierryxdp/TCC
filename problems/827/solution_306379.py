def qtd_divisores(numero):
    
    divisores = []
    contador = 0
    
    for i in list(range(1, numero+1)):
        
        if numero % i == 0 and numero > 0:
            
        	divisores.append[i]
            
            contador += 1
            
    return (contador)