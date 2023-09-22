def insere(lista_numero,n):
    """Retorne uma função que dada uma lista de numeros (inteiros) e um numero inteiro, retorne uma nova lista com os números ordenados de forma crescente. list, int -> list
    Parâmetros:
    lista_numero = lista desejada
    n = numero a se adicionar."""
    lista_vazia = []
    list.extend(lista_vazia,lista_numero)
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero