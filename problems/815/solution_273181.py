def insere(lista_numero,n):
    if n not in lista_numero:
        lista_numero = lista_numero + [n]
        
        lista_numero =s orted(lista_numero)
        
        x = list.index(lista_numero,n)
        
        return lista_numero[(x+1):len(lista_numero)]
    else:
        lista_numero = sorted(lista_numero)
        x = list.index(lista_numero,n)
        return lista_numero[(x+1):len(lista_numero)]