def acima_da_media(lista):
    """coment"""
    list.sort(lista)
    media=sum(lista)/len(lista)
    maior_que_a_media=[n for n in lista if n > media]
    return maior_que_a_media