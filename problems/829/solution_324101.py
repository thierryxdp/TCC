def soma_h (N):
    '''Função que recebe o parametro N de termos e retorna o somatório 
    da sequência H de termos até o enésimo termo
    int -> float'''
    somarH = 0
    for numero in range(1, N+1):
        somarH= somarH + 1/numero
	return round(somarH, 2)