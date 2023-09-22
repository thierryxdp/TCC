def qtd_divisores(n):
    qtd = 0
    
    for i in range(1,n+1):
        if n%i == 0:
            # se é divisor, mais um divisor
            qtd += 1
            print(i)
            
    return qtd