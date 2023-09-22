def acima_da_media (lista_notas):
    '''Dado uma lista de notas retorna, em ordem crescente, uma lista
    com as notas acima da media
    list->list'''
    media = sum(lista_notas)/len(lista_notas)
    return maiores(lista_notas,media)
def maiores(lista_notas,media):
    a=([i for i in lista_notas if i > media])
    return sorted(a)