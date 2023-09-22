def insere(lista_numero, n):
    """retorna uma lista com seus numeros ordenados em ordem crescente. list,int-->list"""
    list.insert(lista_numero,0,n)
    list.sort(lista_numero)
    
    return lista_numero