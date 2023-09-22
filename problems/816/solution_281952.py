def maiores(lista_numero,n):
    """Dada uma lista de números inteiros e um número inteiro n.
    A função retorna outra lista com apenas os números maiores que n
    da lista dada como parâmetro, ordenados em ordem crescente.
    A lista deve ser escrita entre colchetes [];
    list, int --> list"""
    if n in lista_numero:
        list.remove(lista_numero,n)
        list.append(lista_numero,n)
        list.sort(lista_numero)
        indice = list.index(lista_numero,n)
        return lista_numero[(indice+1):]
    if n not in lista_numero:
        list.append(lista_numero,n)
        list.sort(lista_numero)
        indice = list.index(lista_numero,n)
        return lista_numero[(indice+1):]