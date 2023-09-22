def insere(lista_numero, n):
    if (n < (lista_numero[0])):
        return [n] + lista_numero
    
    elif n > (len(lista_numero)//2):
        return lista_numero + [n]
    
    elif n > (len(lista_numero)-1):
        return lista_numero + [n]