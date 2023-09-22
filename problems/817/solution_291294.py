def maiores(lista, n):
    """Função que dada uma lista de numeros inteiros e um numero inteiro n,
    retorna outra lista que contenha todos os numeros da lista original maiores
    que n.
    Dados de entrada: list, int.
    Dados de saida: list."""
    list.append(lista, n)
    list.sort(lista)
    if n not int lista:
        return lista[list.index(lista, n) + 1:]
    return lista[list.index(lista, n) + 2:]

def acima_da_media(notas):
    """Função que dada uma lista com notas dos alunos de uma turma, retorne uma
    lista ordenada com as notas que ficaram acima da da media.
    Dados de entrada: list.
    Dados de saida: list."""
    soma = sum(notas)
    quantidade = len(notas)
    media = soma/quantidade
    if media not in notas:
        return maiores(notas, media)
    return maiores(notas, media)