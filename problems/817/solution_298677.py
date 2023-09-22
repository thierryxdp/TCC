def maiores(lista, n):
    '''Retorna uma lista, em ordem crescente, com os número 
    maiores que n presentes na lista dada como parâmetro (com
    números inteiros)
    list, int --> list'''
    list.append(lista, n)
    list.sort(lista)
    indice = list.index(lista, n)
    maiores = lista [indice + 1:]
    return maiores

math.import
def acima_da_media(notas):
    '''Retorna uma lista com as notas dos alunos que
    ficaram acima da média, a partir da lista com as
    notas dada como parâmetro
    list --> list'''
    media = (sum(notas))/len(notas)
    acima_med = maiores(notas, math.ceil(media))
    return acima_med