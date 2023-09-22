def qtd_divisores(N):
    if N < 0:
        N * -1
    NUM = 1
    F = 0
    while NUM !=N:
        if N%NUM==0:
            F = F + 1
    	NUM = NUM + 1
    return F+1