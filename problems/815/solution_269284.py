def insere(lista_numero,n):
    """Esta função que dada uma lista ordeanada(crescente) de números inteiros e
    um número inteiro 'n', inclui 'n' na posição correta de tal maneira que
    a lista continue ordenada.
    Entrada: lista(int, int) ; Saída: lista(int)"""
    
    list.append(lista_numero, n)
    list.sort(lista_numero)
    return lista_numero