def qtd_divisores(num):
    qtd = 1
    
    if(num > 0):
        for i in range(1, num):
            if(num % i == 0):
                qtd += 1
            
        return qtd
    else:
        return 0