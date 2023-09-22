def maiores(numeros, n):
    """Função que, dada uma lista de números inteiros e um
    número inteiro n, retorna uma outra lista, que contém
    todos os números da lista original maiores que n, ordenados
    em ordem crescente.
    list, int -> list"""
    if n not in numeros:
        list.append(numeros, n)
    list.sort(numeros)
    posicao = list.index(numeros, n)
    lista = numeros[posicao:]
    list.remove(lista, n)
    return lista

def acima_da_media(notas):
    """Função que, dada uma lista com as notas dos alunos
    de uma turma, retorna uma lista ordenada com as notas
    que ficaram acima da média.
    list -> list"""
    media = int(sum(notas)/len(notas))
    return maiores(notas, media)