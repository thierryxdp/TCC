def acima_da_media(notas):
    ''' Retorna apartir de uma lista de notas, outra lista com aquelas que são maiores
        do que a média entre elas
        list -> list'''
    media = sum(notas)/len(notas)
    notas_acima = list()
    lista = ([n for n in notas if n > media])
    list.sort(lista)
    return lista