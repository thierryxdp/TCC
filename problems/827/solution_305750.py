def qtd_divisores(num):
    
    
    contador=0
    
    for divisores in range(2,num):
        if num%divisores!=0:
            contador=contador+1
            
    return contador