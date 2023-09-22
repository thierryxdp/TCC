def maiores(lista_numero,n):
    maiores=[item for item in lista_numero if item > n]
	return sorted(maiores)
'''dado um numero e uma lista retorna uma nova lista com os numeros maiores
que ele
list,int->list'''
def acima_da_media (notas):
    soma= sum(notas)
    quantasNotas=len(notas)
    mediaNotas= soma//quantasNotas
    return maiores(notas,mediaNotas)
'''funcao que calcula a media de uma turma e retorna uma lista das 
notas que estao acima da media geral da turma
list->list'''