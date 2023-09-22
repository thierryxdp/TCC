def maiores(lista,n):
    '''Dada uma lista constituída de números inteiros e um
    inteiro n forma-se outra lista ordenada a partir dos
    maiores que n.
    list, int -> list'''
    list.append(lista,n)
    list.sort(lista)
    a=list.index(lista,n)
    return lista[a+1:]
def acima_da_media(lista):
    '''Dada uma lista com a nota dos alunos essa função
    retorna uma lista ordenada com as notas acima da média.
    list -> list'''
    media=sum(lista)/len(lista)
    if media in lista:
        list.remove(lista,media)
        return maiores(lista,media)
    else:
        return maiores(lista,media)