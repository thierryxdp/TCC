def acima_da_media(lista):
    media=sum(lista)/len(lista)
    listanova = [x for x in lista if x>media]
    listanova.sort()
    return listanova