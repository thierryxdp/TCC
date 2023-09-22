def soma_h(numero):
    '''
    	Funcao que recebe um numero (N) inteiro e retorna o 
        valor de H com N termos
        H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N
        int -> float
    '''
    total = 0
    for i in range(2, numero+1):
        total += 1/i
    x = total + 1
    return round(x, 2)