def maiores(lista_numeros, n):
    """Função que, dada uma lista de números inteiros
    e um número inteiro n, retorna outra lista que contenha
    todos os números da lista original maiores que n,
    ordenados em ordem crescente.
    list , int -> list"""
    lista = [n]
    lista1 = lista_numeros + lista
    list.sort(lista1)
    return lista1[(list.index(lista1, n)+1):]

def acima_da_media(lista_notas):
    """Função que, dada uma lista com as notas dos alunos 
    de uma turma, retorna uma lista ordenada com as notas que
    ficaram acima da média.
    list -> list"""
    media = int(sum(lista_notas)/len(lista_notas))
    return maiores(lista_notas, (media + 1))