def filtraMultiplos(lista,digito):
	""" Função que dada uma lista de numeros inteiros, retorna uma nova lista contendo apenas os numeros pares.
ent> string
saida> lista
"""
	pares=()
	proximo=0
	while proximo<len(lista):
		if lista[proximo]%digito==0:
			pares+=[lista[proximo]]
		proximo=proximo+1
	return pares