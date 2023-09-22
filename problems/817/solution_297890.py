def maiores(lista, n):
    '''funçao que recebe uma lista de numeros inteiros e retorna 
    uma nova lista com numeros interios maiores que n. list, int -- list'''
    lista1 = [x for x in lista if x > n]
    list.sort(lista1)
    return lista1
def acima_da_media(l1, media):
    '''funcao que recebe uma lista com notas de alunos e retorna 
    uma lista com as notas acima da media. list --- list'''
    return maiores(l1, media)