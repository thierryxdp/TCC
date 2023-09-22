def lingua_p(palavra):
    lista = list(palavra)
    n = 0
    while n < len(lista):
        if lista[n] in "a":
            list.insert(lista, n + 1, 'pa')
        if lista[n] in "e":
            list.insert(lista, n + 1, 'pe')
        if lista[n] in "i":
            list.insert(lista, n + 1, 'pi')
        if lista[n] in "o":
            list.insert(lista, n + 1, 'po')
        if lista[n] in "u":
            list.insert(lista, n + 1, 'pu')
        if lista[n] in "á":
            list.insert(lista, n + 1, 'pá')
        if lista[n] in "é":
            list.insert(lista, n + 1, 'pé')
        if lista[n] in "í":
            list.insert(lista, n + 1, 'pí')
        if lista[n] in "ó":
            list.insert(lista, n + 1, 'pó')
        if lista[n] in "ú":
            list.insert(lista, n + 1, 'pú')
        n = n + 1
    return ''.join(lista)