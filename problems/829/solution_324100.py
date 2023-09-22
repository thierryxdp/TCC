def soma_h (N):
    '''Função que recebe o parametro N de termos e retorna o somatório 
    da sequência H de termos até o enésimo termo
    int -> float'''
    somar_H = 0
    for numero in range(1, N+1):
        soma_H= soma_H + 1/numero
	return round(somar_H, 2)