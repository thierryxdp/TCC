def insere(lista_numero, n):
    """Funcao que retorna a lista_numero, com o acrescimo de um numero n,
    de forma ordenada(crescente).
    Entrada: list(int), int
    Saída: lista(int)
    
    Parameters: 
    lista_numero: Lista ordenada de forma crescente
    n: número a ser incrementado na lista"""

    lista_numero.append(n)
    lista_numero.sort()
    
    return lista_numero