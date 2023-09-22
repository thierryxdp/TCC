def maiores(lista,n):
    '''Dada uma lista constituída de números inteiros e um
    inteiro n forma-se outra lista ordenada a partir dos
    maiores que n.
    int ->int'''
    list.append(lista,n)
    list.sort(lista)
    a=list.index(lista,n)
    return lista[a+1:]
def acima_da_media(lista):
    '''Dada uma lista com a nota dos alunos essa função
    retorna uma lista ordenada com as notas acima da média'''
    media=sum(lista)/len(lista)
    return maiores(lista,n)