def insere(lista_numero,n):
    """Retorne a lista com de entrada com o parâmetro n na posição correta(crescente)"""
    nova = lista_numero + n
    list.sort(nova)
    return nova