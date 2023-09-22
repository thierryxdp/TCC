def acima_da_media(lista_notas):
    '''da somente as notas que estão acima da media das notas na lista'''
    a = sum(lista_notas)/len(lista_notas)
    if a in lista_notas:
        list.remove(lista_notas,a)
        list.append(lista_notas,a)
        list.sort(lista_notas)
        b = list.index(lista_notas,a)
        c = lista_notas[b+1:]
        return c
    else:
        list.append(lista_notas,a)
        list.sort(lista_notas)
        b = list.index(lista_notas,a)
        c = lista_notas[b+1:]
        return c