def lingua_p(palavra):
    lista = []
    for letra in palavra:
        if str.lower(letra) in 'aeiouáãâéêíîóõôúû':
            list.append(lista, letra)
            list.append(lista, 'p')
            list.append(lista, letra)
        else:
            list.append(lista, letra)
    return str.lower(str.join(lista, ''))