def insere(lista_numero, n):
    """Dada uma lista em ordem crescente de números inteiros e um
    inteiro "n", a função inclui o número n na posição certa de 
    forma que a lista permaneça ordenada.
    list, int -> list"""
    
    lista = lista_numero
    list.append(lista, n)
    list.sort(lista)
    
    return lista