def insere(lista_numero,n):
    #insere o valor na lista e mantém a ordem.
    #list,int-list
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero