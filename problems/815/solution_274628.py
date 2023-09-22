def insere(lista_numero,n):
    '''função que insere um número n dentro de uma lista ordenada(crescente) em sua devida posição
       list,int -> list'''
    lista=list.append(lista_numero,n)
    lista=list.sort(lista_numero)
    return lista