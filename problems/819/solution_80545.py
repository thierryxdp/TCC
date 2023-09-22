def filtraMultiplos(lista,n):
    """ funcao recebe uma entrada de uma lista de numeros e retorna outra lista contendo todos elementos da lista original que forem dividido por n"""
	"""lista->lista"""
lista2=[]
proximo=0
	while proximo<len(lista):
    if lista[proximo]%n==0:
        lista2=lista2+[lista[proximo]]
        proximo=proximo+1
				return lista2