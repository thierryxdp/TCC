def insere(lista_numero:list,n:int)->list:
    lista_numero.append(n)
    list.sort(lista_numero)
    return lista_numero