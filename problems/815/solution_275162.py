def insere(lista_numero,n):
    """Função que dada uma lista ordenada de números crescentes
    inteiros e um número inteiro n, inclua n na posição correta.
    list -> list"""
    y=[n]
    list.extend(lista_numero,y)
    list.sort(lista_numero)
    return lista_numero