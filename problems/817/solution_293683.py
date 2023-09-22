def acima_da_media(lista):
    '''funcao retorna as notas acima da media. list->list'''
    lista2=[]
    for i in range(len(lista)):
        if sum(lista)/len(lista)<lista[i]:
            lista2.append(lista[i])
    lista2.sort()
    return lista2