def qtd_divisores(N):
    NUM = 1
    F = 0
    while NUM != N:
        if N+1 % NUM == 0:
            F = F + 1
    	NUM = NUM + 1          
    return F