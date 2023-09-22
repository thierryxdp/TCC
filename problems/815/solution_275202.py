def insere(lista_numero,n):
    """Recebe uma lista de números e um inteiro e retorna uma única lista com o inteiro incluso na lista e em ordem crescente.
    Assinatura: list,int -> list"""
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return sorted(lista_numero)