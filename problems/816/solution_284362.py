def maiores(lista_numero, n):
    """dada uma lista de números inteiros e um inteiro "n", a função
    retorna uma lista com os com os números maiores que "n" em ordem
    crescente.
    list, int -> list"""
    
    lista = lista_numero
    list.append(lista, n)
    list.sort(lista)
    
    indice = list.index("lista", "n")
    
    return lista[indice+1:]