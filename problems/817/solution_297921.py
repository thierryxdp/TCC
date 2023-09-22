def maiores(lista,n):
    '''Dada uma lista de numeros inteiros e um inteiro n,
    retorna uma lista que contenha os numeros da lista
    original que são maiores que n, ordenados de forma
    crescente; list, int -> list'''
    lista_nova = lista
    list.append(lista_nova,n)
    list.sort(lista_nova)
    inicio = list.index(lista_nova,n)
    return lista_nova[(inicio+1):]

def acima_da_media(lst):
    '''Dada uma lista com as notas dos alunos de uma turma,
    retorna uma lista ordenada de forma crescente com as notas
    que ficaram acima da media; list -> list'''
    media = sum(lst)/len(lst)
    if len(lst)==1 or len(lst)==0:
        return []
    elif media in lst:
        list.remove(lst, media)
        return maiores(lst,media)
    else:
    	return maiores(lst,media)