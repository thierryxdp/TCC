def maiores(lista_numero,n):
    maiores=[item for item in lista_numero if item > n]
	return sorted(maiores)
def acima_da_media (notas):
    soma= sum(notas)
    quantasNotas=len(notas)
    mediaNotas= soma//quantasNotas
    return maiores(notas,mediaNotas)