def qtd_divisores(num):
	'''Retorna quantos divisores num tem
	int -> int'''
   
	nDivs = 0
	for div in range(1,num+1):
		if num%div == 0:
			nDivs += 1

	return nDivs