def insere(lista_numero,n):
    """Recebe uma lista em ordem crescente de números inteiros, incluindo
    um número inteiro /n/, e retorne a lista com o número /n/ na posição
    correta (mantendo a lista em ordem crescente).
    assinatura: list, int -> list
    testes:
    insere([1,2,3,6],5) == [1, 2, 3, 5, 6]
    insere([9,10,11,14],12) == [9, 10, 11, 12, 14]
    """
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero