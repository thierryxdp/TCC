def insere(lista_numero, n):
    '''funcao que retorna uma lista com
    o interio n ordenado na lista dada 
    como parametro
    entrada: lista, inteiro
    saida: lista
    '''
    lista_n= list.insert(lista_numero,0,n)
    lista_ordenada= list.sort(lista_n)
    return lista_ordenada