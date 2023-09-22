def primo (inteiro):
    '''Função que recebe um número inteiro e retorna True se o número é primo,
    mas se o número não for primo a função retorna False
    int -> bool'''
    arrendonda = round(numero**(1/2))
    for indice in range(2, teto + 1):
        if numero % indice == 0:
            return False
	return True