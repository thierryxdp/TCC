def maiores(lista,m):
    '''função que dada uma lista de números inteiros e um número inteiro (n), retorna outra lista, que contenha todos os números da lista original maiores que (n), ordenados em ordem crescente; list, int -> list'''
    list.append(lista,m)
    list.sort(lista)
    p=list.index(lista,m)
    if lista[p+1]==m:
        return[]
    else:
        return lista[p+1:]
def acima_da_media(lista):
    '''função que dada uma lista com as notas dos alunos de uma turma, retorne uma lista ordenada com as notas que ficaram acima da média; list -> list'''
    m=(sum(lista))/(len(lista))  
    return maiores(lista,m)