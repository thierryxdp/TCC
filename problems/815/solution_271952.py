def insere(lista_numero, n):
    if (n > (lista_numero[0])) == True:
        return [n] + lista_numero
    
    elif n > (len(lista_numero)-1):
        return lista_numero + [n]
    
    elif n > (len(lista_numero)-1):
        return lista_numero + [n]