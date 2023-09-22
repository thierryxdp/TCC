def maiores(lista,n):
    '''Retorna outra lista com todos os numeros maiores que n
    em ordem crescente; list,int->list'''
    if n in lista:
        lista.sort(lista)
        lista2=lista[list.index(lista,n) + 1:]
        return lista2
    else:
        list.append(lista,n)
        list.sort(lista)
        lista2= lista[list.index(lista,n) + 1:]
        return lista2
    
def acima_da_media(lista):
    '''Retorna uma lista ordenada com as notas que ficaram
    acima da media; list->list'''
    media=(sum(lista)/len(lista))
    media1=maiores(lista,media)
    return media1