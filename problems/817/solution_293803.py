def maiores(lista,n):
    
    if n not in lista:
        list.append(lista,n)
    list.sort(lista)
    ind= list.index(lista,n)
    lista1= lista[ind+1:]
    return lista1

def acima_da_media(lista):
    """funcao que aproveita a funcao da questao 4, e dada uma lista de notas,
    retorna uma nova lista ordenadas com as notas que ficaram acima da media. list->list."""
    media=sum(lista)/len(lista)
    return maiores(lista,media)