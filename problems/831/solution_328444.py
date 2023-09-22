def lingua_p(palavra):
    vogais = ['a','e','i','o','u','á','à','ã','é','ê','í','ó',õ','ô','ú']
    i = 0
    palavrinhaP = []
    for letrinha in palavra:
        if letrinha in vogais:
            list.append(palavrinhaP, letrinha)
            list.append(palavrinhaP, 'p')
            list.append(palavrinhaP, letrinha)
        else:
            list.append(palavrinhaP, letrinha)
    return str.lower(str.join('',palavrinhaP))