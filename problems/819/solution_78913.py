def filtraMultiplos(lista,n):
    '''Função que ao receber uma lista de numeros, retorna uma lista contendo os multiplos do parametro n'''
    '''list, int -> list'''
    lista = []
    i = 0
    while i <= len(lista):
        if (lista[indice] %n) == 0:
            lista = lista + lista[indice]
            indice = indice + 1
    return lista