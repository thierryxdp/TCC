def insere(lista_numero, n ):
    """Função que dada uma lista de numeros inetiros e um numero n, inclua n na posição 
    correta, de maneira que a lista continue ordenada
    int, int --> int"""
    acrescente = list.append(lista_numero, n)
    tam = len(acrescente)
    lista_ordenada = list.sort(acrescente)
    return lista_ordenada