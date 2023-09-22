def primo (numero: int) -> bool:
    """A função recebe um número inteiro positivo e verifica se ele é primo ou não. Caso seja primo retorna um booleano, True. Caso não retorna False"""
	
    eh_primo = []
    for indice in list(range(1,numero+1)):
        if (numero % numero_range[indice] == 0):
            list.append(eh_primo,numero_range[indice])
	return len(eh_primo) == 2