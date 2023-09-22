def filtraMultiplos(lista,n):
    """Função que filtra os multiplos de (n) de uma (lista) e retorna
    uma segunda lista composta pelos multiplos de (n).
    list, int -> list"""

    i=0
    while i<len(lista):
        if lista[i]%n != 0:
            del lista[i]      
        i=i+1       
    return lista