def qtd_divisores(num):
    qtd = 0
    
    if(num > 0):
        for i in range(1, num):
            if(num % i == 0):
                qtd += 1
            
        return qtd
    else:
        return 0