def maiores(lista_numero,n):
    """Dada uma lista de numeros inteiros e um numero inteiro n, retorna outra lista, que contem todos os numeros da lista original maiores que n, ordenados em ordem crescente. str -> str"""
    lista_numero.append(n)
    list.sort(lista_numero)
    x=lista_numero.index(n)
    del(lista_numero[:x+1])
    return lista_numero

def acima_da_media(notas):
    """Dada uma lista com as notas dos alunos de uma turma, retorna uma lista ordenada com as notas que ficaram acima da media. list -> list"""
    media=(sum(notas))/(len(notas))
    maiores(notas,media)
    return notas