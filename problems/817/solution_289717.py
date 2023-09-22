def acima_da_media(lista):
    """dada as notas dos alunos, retorna uma lista ordenada com as notas
    acima da media
    list->list"""
    med = sum(lista)/len(lista)
    if med in lista:
        list.sort(lista)
        l1 = list.index(lista,med)
        return lista[l1+1:]
    else:
        list.append(lista,med)
        list.sort(lista)
        l1=lista.index(med)
        return lista[l1+1:]