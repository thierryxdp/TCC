def maiores (lista,n):
    '''Função de dada uma lista, retorna outra lista coms os nº maiores que n em ordem crescente.
    list, int -> list'''
    media = sum(lista)/len(lista)
    list.append(media)
    list.sort(lista)
    i = list.index(lista,media) 
    return lista[i+1:]