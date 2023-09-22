def faltante(lista):
    """funcao que dada uma lista com numeros de 1 a n indica qual numero esta faltando na lista"""
	"""list->int"""
    primeiro = 0
    ultimo = [-1]
    while ultimo != -1:
        if primeiro in lista:
            primeiro = primeiro + 1
        
        else:
            return primeiro