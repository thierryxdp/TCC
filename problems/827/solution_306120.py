def qtd_divisores(N):
    NUM = 1
    F = 0
    while NUM+1 != N:
        if N % NUM == 0:
            F = F + 1
    	NUM = NUM + 1          
    return F