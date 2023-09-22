def maiores(lista_numeros,n):
    """Função que, dada uma lista de números inteiros e um número inteiro n, retorna outra lista, contendo todos os números da lista original maiores que n, ordenados em ordem crescente
    entrada: list, int
    saída: list"""
    lista_incluida=list.append(lista_numeros,n)
    lista_ordenada=list.sort(lista_numeros)
    lista_modificada=list.index(lista_numeros,n)
    return lista_numeros[lista_modificada+1:]

def acima_da_media(lista_notas):
    """Função que, dada uma lista com as notas dos alunos de uma turma, retorna uma lista ordenada com as notas que ficaram acima da média
    entrada: list
    saída:list"""
    media=(sum(lista_notas))/len(lista_notas)
    if media in lista_notas:
        remove_media=list.remove(lista_notas,media)
        return maiores(lista_notas,media)
    else:
        return maiores(lista_notas,media)