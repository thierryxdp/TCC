def qtd_divisores(N):
    NUM = 1
    X = N + 1
    F = 0
    while NUM != X:
        if X % NUM == 0:
            F = F + 1
    	NUM = NUM + 1          
    return F