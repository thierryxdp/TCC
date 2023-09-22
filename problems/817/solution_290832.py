def acima_da_media(notas):
    ''' Retorna '''
    media = sum(notas)/len(notas)
    notas_acima = list()
    lista = ([n for n in notas if n > media])
    list.sort(lista)
    return lista