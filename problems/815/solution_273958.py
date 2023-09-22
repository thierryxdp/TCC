def insere(l, n):
    'Recebe uma lista e um numero n, adiciona o numero a lista e ordena ela em ordem alfabética'
    l= l + [n]
    list.sort(l)
    return l