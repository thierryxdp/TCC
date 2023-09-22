def repetidos(nums):
    '''função que retorna a frenquencia em que um numero dentro de uma lista é igual ao seu antecessor'''
    '''list->int'''
    cont=0
    acumulador = 0
    while cont < len(nums):
    	if nums[cont]==nums[cont-1]:
        	cont += 1
        	acumulador += 1
		else:
            cont += 1
	return acumulador