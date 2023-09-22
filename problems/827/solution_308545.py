def qtd_divisores(numero):
    '''Função que verifica quantos divisores um número qualquer tem.
	int-->int'''
    i = 0
    for elemento in range(1,numero):
        if numero % elemento == 0:
            i += 1

    if numero < 0:
        return i
  
	elif numero == 0:
   		return 0
	else:
    	return i + 1