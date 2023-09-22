def insere(lista_numero,n):
    """Funcao que inclui um numero em em lista crescente sem que ela 
    perca essa caracteristica
    entrada: lista, int
    saida: lista"""
    x = lista_numero + [n]
    return list.sort(x)