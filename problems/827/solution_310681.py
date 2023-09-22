def qtd_divisores(num):
    qtd = 2
    
    if(num > 1):
        for i in range(2, num-1):
            if(num % i == 0):
                qtd += 1
            
        return qtd
    elif(num < 0):
        return "error"
    else:
        return 1