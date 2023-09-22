def insere(lista_numero, n):
    """Função que dada uma lista ordenada crescente de números inteiros e um numero inteiro n, inclua n na posição,
    lista ,int --> lista"""
    
    lista = list.append(lista_numero, n)
    
    lista = list.sort(lista)
    
    return lista2