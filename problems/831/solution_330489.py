def lingua_p(palavra):
    nova = []
    vogal = 'aeiou'
    for letra in palavra:
        if letra == vogal:
            nova.append(vogal)
        else:
            nova.append(letra)

    return ''.join(nova)