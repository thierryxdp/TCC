def acima_da_media(lista):
    '''retorna as notas acima da media em ordem crescente
    list -> list'''
    list.append(lista, 5)
    list.sort(lista)
    x=lista.index(5)
    lista_nova=lista[x:]
    list.remove(lista_nova, 5)
    
    return lista_nova