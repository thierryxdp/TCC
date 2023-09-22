def insere(lista_numero, n):
    """Função que insere um número inteiro n em um lista, de forma que esta continue ordenada
    list, int -> list"""
    
    lista_final = lista_numero + [n]
    lista_final.sort()
    
    return lista_final