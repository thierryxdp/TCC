def qtd_divisores(num):
    
    qtd = 0
    for div in range(1,num+1):
        
        if not num%div:
            qtd+=1
    
    return qtd