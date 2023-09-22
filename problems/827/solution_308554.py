def qtd_divisores(numero):
    '''Função que verifica quantos divisores um número qualquer tem.
	int-->int'''
    i = 0
    for elemento in range(1,numero+1):
        if numero % elemento == 0:
            i += 1
    return i