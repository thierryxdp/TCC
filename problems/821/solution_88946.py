def fatorial(num):
    '''Função que dado um número (inteiro e maior ou igual a 0)
    retorne seu fatorial
    int -> int'''
    if num != 0:
        acumulador = 1
        fator = 1
        while fator != num + 1:
            acumulador *= fator
            fator += 1
		return acumulador
    else:
        return 1