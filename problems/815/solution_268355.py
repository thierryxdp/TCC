def insere(lista_numero, n ):
    """Função que dada uma lista de numeros inetiros e um numero n, inclua n na posição 
    correta, de maneira que a lista continue ordenada
    int, int --> int"""
    acrescente = (lista_numero + n) 
    ordem = acrescente  .sort(lista)
    return ordem