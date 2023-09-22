def maiores (lista_numero,n):
    '''Função de dada uma lista, retorna outra lista coms os nº maiores que n em ordem crescente.
    list, int -> list'''
    media = sum(lista_numero)/len(lista_numero)
    list.append(lista_numero,n)
    list.sort(lista_numero)
    i = list.index(lista_numero,media) 
    return lista_numero