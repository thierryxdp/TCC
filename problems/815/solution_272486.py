def insere(lista_numero, n):
    '''funcao que retorna uma lista com
    o interio n ordenado na lista dada 
    como parametro
    entrada: lista, inteiro
    saida: lista
    '''
    lista_n= list.extend(lista_numero,n)
    return list.sort(lista_n)