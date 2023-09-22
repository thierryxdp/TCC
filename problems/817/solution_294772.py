def insere(lista_numero,n):
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero
def maiores(lista_numero,n):
    ordem= insere(lista_numero,n)
    return ordem[list.index(ordem,n)+1:]
def acima_da_media(notas):
    """A função retorna uma lista ordenada com as notas
	que ficaram acima da média, utilizando duas funções
	desenvolvidas nos exercícios anteriores; list->list"""
    quantidade=len(notas)
    Sum=sum(notas)
    media=int((Sum/quantidade))+1
    notas_maiores=maiores(notas,media)
    return notas_maiores