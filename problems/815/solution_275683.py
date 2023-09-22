def insere(lista_numero,n):
    lista2 = lista_numero.append(n) 
    sort(lista2, key=int)
    return lista2