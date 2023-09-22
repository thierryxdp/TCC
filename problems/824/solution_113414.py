def uppCons(frase):
    prox = 0
    fraseLista = []
    while prox < len(frase):
        if frase[prox] != 'A' or 'E' or 'I' or 'O' or 'U' or 'a' or 'e' or 'i' or 'o' or 'u':
            letra = frase[prox].upper()
            list.append(fraseLista, letra)
        prox = prox + 1
    return ''.join(fraseLista)