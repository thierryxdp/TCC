def total( lista, produtos):
    """Funcao que dada uma lista de compras e o preço de cada produto
    retorna a soma do valor total da lista
    list, dict --> float"""
    valor = 0
    for i in range(len(lista)):
        produto = lista[i]
        valor = valor + produtos[produto]
    return valor