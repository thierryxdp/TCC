1)	def filtraMultiplos(lista,n):
    """essa funcao,recebe uma lista de numeros e um numero e retorna outra lista contendo todos os elementos da lista original que forem divisiveis por n"""
	"""int->int"""
    multiplo=[]
    i=0
    
    while i < len(lista):
        if lista[i]%n==0:
            multiplo=multiplo+[lista[i]]
        i=i+1
    return multiplo