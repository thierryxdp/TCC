def total(lista, produtos):
    ''' retorna uma lista contendo a quantidade de vezes que as palavras
    aparecem em uma frase.
    list, dict -> float'''

    preco = 0

    for produto in lista:
        if produto in produtos[produto]:
            preco = preco + produtos[produto]
    return preco