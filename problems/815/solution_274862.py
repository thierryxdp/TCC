def insere(lista_numero,n):
    """Recebe uma lista em ordem crescente de números inteiros, incluindo
    um número inteiro /n/, e retorne a lista com o número /n/ na posição
    correta (mantendo a lista em ordem crescente).
    assinatura: list, int -> list
    testes:
    insere([0,2,4,6],5) == [0, 2, 4, 5, 6]
    insere([1,2,3,4],0) == [0, 1, 2, 3, 4]
    """
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero