def qtd_divisores(num):
    
    contador=0
    
    for i in range(int(num)):
        if num%i==0:
            contador=contador+1
            
    return contador