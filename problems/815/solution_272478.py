def insere(lista_numero, n):
    '''funcao que retorna uma lista com
    o interio n ordenado na lista dada 
    como parametro
    entrada: lista, inteiro
    saida: lista
    '''
    lista_numero_n= list.append(lista_numero,n)
    lista_ordenada= list.sort(lista_numero_n)
    return lista_ordenada