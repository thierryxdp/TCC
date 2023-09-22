def filtraMultiplos (lista,n):
    """Funcao que filtra os multiplos de um numero n;
    Entrada: list, int
    Saida: list"""
    
    listao = []
    indice = 0
    
    while indice < len(lista):
        if lista[indice]%n == 0:
            listao = listao + lista[indice]
        indice = indice + 1
    return listao