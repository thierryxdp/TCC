def maiores(lista, n):

    list.insert(lista,1,n)
    list.sort(lista)
    indice = list.index(lista,n) + 1
    return lista[indice:]

def acima_da_media(lista):
    '''retorna uma lista com as notas de alunos acima da media em ordem crescente dada uma 
    lista com as notas.
    list -> list'''
    return maiores(lista, 7)