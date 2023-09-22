def acima_da_media(lista):
    '''retorna as notas acima da media em ordem crescente
    list -> list'''
    list.append(lista, 7)
    list.sort(lista)
    x=lista.index(7)
    lista_nova=lista[x:]
    list.remove(lista_nova, 7)
    
    return lista_nova