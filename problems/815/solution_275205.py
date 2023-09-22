def insere(lista_numero, n):
    """retorna n na posição correta
    list,int->list"""
    
    lista_numero.append(n)
    lista_numero.sort(n)
    
    return lista_numero