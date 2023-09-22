def qtd_divisores(num):
    
    contador=1
    
    for x in range(1,num):
        if num%x==0:
            contador=contador+1
            
    if num<0:
        return 0
            
    return contador