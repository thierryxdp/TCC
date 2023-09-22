def qtd_divisores(num):
    
    contador=1
    
    for x in num:
        if num%x==0:
            contador=contador+1
            
    return contador