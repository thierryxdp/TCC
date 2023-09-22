def insere(lista_numero,n):
    '''recebe uma lista ordenada de forma crescente e devolver
    essa lista com a inclusão do numero n na posição n de forma q ainda
    seja crescente'''
    list1= list.insert(lista_numero, n, n)
    list2= list.sort(list1)
    return list2