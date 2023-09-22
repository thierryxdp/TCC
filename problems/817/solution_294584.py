def acima_da_media(listanotas):
    '''funcao que retorna uma lista ordenada com as notas
    que ficaram acima da media; list->list'''
    h= sum(listanotas)//len(listanotas)
    if h in listanotas:
        list.sort(listanotas)
        f=list.index(listanotas, h)
        return listanotas[f+1:]