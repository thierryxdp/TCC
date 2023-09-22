def insere(lista_numero,n):
    """Recebe uma lista em ordem crescente de números inteiros, incluindo
    um número inteiro /n/, e retorne a lista com o número /n/ na posição
    correta em ordem crescente.
    assinatura: list, int -> list
    testes:
    insere([22,2],11) == [2, 11, 22]
    insere([10,12,14],16) == [10, 12, 14, 16]
    """
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero