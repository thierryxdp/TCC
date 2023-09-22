def maiores(lista_numeros, n):
    """Dada uma lista de números inteiros e um número inteiro n, retorna outra lista,
    que contenha todos os números da lista original maiores que n;
    list, int -> list"""
    list.append(lista_numeros, n)
    list.sort(lista_numeros)
    lista_maiores = lista_numeros[list.index(lista_numeros, n) + 1:]
    return lista_maiores

def acima_da_media(lista):
    """Dada uma lista com as notas dos alunos de uma turma, retorna uma lista ordenada
    com as notas que ficaram acima da média;
    list -> list"""
    media = sum(lista)/len(lista)
    return maiores(lista, media)