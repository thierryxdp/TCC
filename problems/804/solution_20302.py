def filtra_pares(numeros):
	'''
    	funcao que recebe 4 numeros, filtrando os pares e adicionando em uma nova tupla
    '''
    
    num1,num2,num3,n4=numeros
    pares=tuple()
    
    if num1 % 2 == 0:
    	pares += (num1,)
    elif num2 % 2 == 0:
    	pares += (num2,)
    elif num3 % 2 == 0:
        pares += (num3,)
    elif num4 % 2 == 0:
        pares += (num4,)
    return pares