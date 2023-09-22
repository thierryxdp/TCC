def maiores(lista,n):
    '''Retorna lista contendo os numeros maiores que n da lista de entrada, em ordem crescente.
    list,int->list'''
    nova_lista=lista[:]
    list.append(nova_lista,n)
    list.sort(nova_lista,reverse=True)
    del nova_lista[list.index(nova_lista,n):]
    list.reverse(nova_lista)
    return nova_lista
def acima_da_media(notas):
    '''Retorna lista com as notas que ficaram acima da media.
    list->list'''
    media=sum(notas)/len(notas)
    return maiores(notas,media)