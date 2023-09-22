def acima_da_media(lista):
    ''' Função que recebe uma lista de notas e retorna todas as notas que ficaram acima da média; list->list'''
    media= sum(lista)/len(lista)
    if media in lista:
        l1= maiores(lista,media)
        list.remove(l1,media)
        l2=l1
        return l2
    else:
        l3= maiores(lista,media)
        return l3