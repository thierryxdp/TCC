def freq_palavras(a):

    lista = a.split

    lista = list(lista)

    dicionario = {}

    for dado in lista:

        dicionario[lista[dado]] = lista.count(dado)

    return dicionario