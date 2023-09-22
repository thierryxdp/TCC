def soma_h(n):
    '''Calcula H de acordo com a formula dada pela questão;
    	int --> float'''
    soma = 0
    for c in range(1, n + 1):
        inverso = (1/c)
        soma += inverso
    return round(soma, 2)