def insere(lista_numero,n):
    """Função que dada uma lista ordenada de números crescentes
    inteiros e um número inteiro n, inclua n na posição correta.
    list -> list"""
    
    list.extend(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero