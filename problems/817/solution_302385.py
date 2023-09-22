def maiores(ls, n):
    lista = []
    for e in ls:
        if e > n:
            lista.append (e)
    list.sort (lista)
    return lista

def acima_da_media (notas):
    """Dada uma lista com as notas, retorna outra lista ordenada com as notas acima da média
    assinatura: list -> list
    testes:
    maiores ([1, 5, 8, 3, 0]) == [5, 8]
    maiores ([1, 9, 0, 3]) == [9]
    """
    elem = len (notas)
    soma = sum (notas)
    media = soma / elem
    return maiores (notas, media)