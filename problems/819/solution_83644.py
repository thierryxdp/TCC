def filtraMultiplos(lista, n):
    """Função que recebe como entra uma lista de números e um
    número, e retorna outra lista contendo todos os elementos
    da lista original que forem divisíveis por n;
    list, int -> list"""
    k = 0
    lista_nova = []
    while k < len(lista):
        if lista[k] % n == 0:
            lista_nova = lista_nova + [lista[k]]
        k = k + 1
    return lista_nova