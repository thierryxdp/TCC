def insere(lista_numero,n):
    list.sort(lista_numero)
    if (n in lista_numero)==True:
        list.insert(lista_numero,list.index(lista_numero,n),n)
        return lista_numero
    else:
        if n>lista_numero[(len(lista_numero)-1)]:
            list.append(lista_numero,n)
            return lista_numero
        if n<lista_numero[0]:
            list.insert(lista_numero,0,n)
            return lista_numero