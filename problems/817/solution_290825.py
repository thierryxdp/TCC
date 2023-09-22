def acima_da_media(lista):
    """essa funcao, dada uma lista com notas,
	 retorna uma lista ordenada com as notas que ficaram acima da media"""
    n_elementos = len(lista)
    media = sum(lista)/n_elementos
    maior = [n for n in lista if n > media]
    return sorted(maior)