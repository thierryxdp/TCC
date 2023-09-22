def maiores(lista_numeros,n):
    """funcao que, dada uma lista de numeros inteiros e um numero inteiro n, retorna uma lista que contenha todos os numeros da lista original maiores que n
    list(int),int--->list(int)"""
    lista_numeros=lista_numeros+[n]
    list.sort(lista_numeros)
    x=list.index(lista_numeros,n)
    return lista_numeros[x+1:]

def acima_da_media(list_notas):
    """funcao que, dada uma lista com as notas de alunos de uma turma, retorna uma nova lista ordenada com as notas acima da media
    list(float)--->list(float)"""
    maiores(list_notas,5)
    return list_notas