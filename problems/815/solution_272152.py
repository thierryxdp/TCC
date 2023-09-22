def insere (lista_numero, n):
    """recebe uma lista de numeros inteiros ordenada em ordem crescente e um
    outro inteiro, e retorna essa lista com o dado inteiro inserido na posicao
    correta
    list => list"""
    
    lista_numero = lista_numero + [n]
    
    return sorted(lista_numero)