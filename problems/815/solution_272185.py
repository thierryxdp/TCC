def insere(lista_numero,n):
    '''a função recebe uma lista númerica e um número,
    o número é adicionado na lista e a lista e ordenada de 
    forma crescente list[int],int ->list[int]
    '''
    numero = lista_numero
    numero.append(n)
    list.sort(lista_numero)
    return lista_numero