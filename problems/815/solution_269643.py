def insere(lista_numero, n):
    """dada uma lista ordenada crescente inclue n na posição correta
    list,int -> list"""
    
    lista_numero.insert(0,n)
    
    return list.sort(lista_numero)