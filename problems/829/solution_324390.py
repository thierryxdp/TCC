def soma_h(n):
    '''Retorna o resultado da soma 1+(1/2)+(1/3)...+(1/n) conforme o
    número inteiro de entrada n, com 2 casas deciamais;
    int -> float'''
    soma=0
    inteiros=list(range(n))+[n]
    inteiros.remove(0)
    for i in inteiros:
        soma=soma+(1/i)
	return round(soma, 2)