def acima_da_media(lista):
    """Dado uma lista como argumento possuindo números do tipo
    int, retorna outra lista apenas com os números maiores que a média
    dos números dessa lista
    lista(int)->lista(int)"""
    list.sort(lista)
    media=sum(lista)/len(lista)
    maior_que_a_media=[n for n in lista if n > media]
    return maior_que_a_media