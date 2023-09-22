def qtd_divisores(num):
    
    contador=1
    
    for div in num:
        if num%div==0:
            contador=contador+1
            
    return contador