def lingua_p(palavra):
    nova = []
    for letra in palavra:
        if letra == 'a':
            nova.append('a')
        if letra == 'e':
            nova.append('e')
        if letra == 'i':
            nova.append('i')
        if letra == 'o':
            nova.append('o')
        if letra == 'u':
            nova.append('u')
        if letra == 'ã':
            nova.append('ã')
        else:
            nova.append(letra)

    return ''.join(nova)