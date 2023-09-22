def maiores(lista,n):
    """função que recebe uma lista de números inteiros e um número inteiro n e retorna
    todos os números da lista original maiores que n. list, int -> list"""
    list.append(lista,n)
    list.sort(lista)
    i = list.index(lista,n)
    novalista = lista[i+1:]
    return novalista
def acima_da_media(lista):
    """função que recebe uma lista com as notas dos alunos de uma turma e retorna a média
    da turma e uma lista ordenada com as notas acima da média. list -> list"""
    media = round(sum(lista)/len(lista),2)
    maioresnotas = maiores(lista,media)
    list.sort(maioresnotas)
    return maioresnotas