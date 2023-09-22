def lingua_p(palavra):
    lista = list(palavra)
    vogais = list('aeiouAEIOU')
    for vogal in vogais:
        if vogal in lista:
            lista.insert(lista.index(vogal), 'p')
    return str.join('', lista)