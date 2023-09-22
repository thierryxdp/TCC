def conta_numero(n,M):
    '''Função que dado um número inteiro n e uma matriz M de
inteiros, retorna a quantidade de vezes que n aparece em M;
	int,list -> int'''
    quant=0
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] == n:
                quant=quant+1
    return quant