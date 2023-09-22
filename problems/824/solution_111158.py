def uppCons(frase):
    lista = list(frase)
    vogais = 'aeiouáâãéêíóôõú'
    for i in lista:
        if i not in vogais:
            lista[lista.index(i)] = i.upper()
    lista2 = ''.join(lista)
    return lista2