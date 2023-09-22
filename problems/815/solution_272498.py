def insere(lista_numero, n):
    """função recebe uma lista de números e um número, 
    adiciona o número à lista, a ordena e retorna lista.
    list, int--> list"""
    
    lista_numero.insert(0, n)
    list.sort(lista_numero)
    return lista_numero