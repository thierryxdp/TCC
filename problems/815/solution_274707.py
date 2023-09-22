def insere(lista_numero,n):
    '''recebe uma lista ordenada de forma crescente e devolver
    essa lista com a inclusão do numero n na posição n de forma q ainda
    seja crescente'''
    listinha = lista_numero
    list.append(listinha, n)
    list.sort(listinha)
    return listinha