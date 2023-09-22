def lingua_p(palavra):
    lista = list(palavra)
    vogais = 'aeiouAEIOU'
    for vogais in lista:
        lista.insert(vogais, 'p')
    return str.join('', lista)