def freq_palavras(a):

    lista = a.split()

    dicionario = {}

    for dado in lista:

        dicionario[dado] = lista.count(dado)

    return dicionario