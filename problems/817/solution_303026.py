def maiores(lista, n):
    """funcao recebe lista e numero inteiro e retorna lista com elementos da entrada a partir do numero inteiro list, int--> list"""
	def acima_da_media(lista):
		"""funcao recebe lista e retorna lista ordenada list--> list"""
		media = int(sum(lista) / len(lista))
		return maiores(lista, media)