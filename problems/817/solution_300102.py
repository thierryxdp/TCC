def insere(lista_numero,n):
    '''funcao que recebe uma lista de numeros ordenada crescente e inclui um numero n de forma que
    continue ordenada. list -> list'''
    list.append(lista_numero, n)
    list.sort(lista_numero)
    return lista_numero

def maiores(lista,n):
    '''recebe uma lista e um numero n, e retorna so os numeros maiores que n da lista em ordem crescente
    list, int -> list'''
    lista = insere(lista,n) 
    lista1 = lista[lista.index(n):]
    list.remove(lista1,n)

    return lista1

def acima_da_media(notas):
    '''recebe uma lista de notas e retorna as notas acima da media
    list -> list'''
    media =  sum(notas)/(len(notas))
    if maiores(notas,media) != media:
    	return maiores(notas,media)
    else:
        return []