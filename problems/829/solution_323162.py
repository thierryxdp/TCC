def soma_h(n):
    '''Função que retorna o somatório de 1 até 1/n
    valor de entrada: int
    valor de saída: float'''
    somatorio= []
    for numero in range (1,n+1):
        somatorio.append(1/numero)
    	return sum(somatorio)